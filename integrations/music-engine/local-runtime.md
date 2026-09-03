Antes de crear la skill he agregado lo siguiente:

Sí. Para probar `music-composer-lab` sin tocar `PATH` ni instalar editable, lo más limpio es usar **el wheel compilado de** **`music-engine`** **dentro de un entorno virtual propio del lab**.

La idea sería:

```text
music-engine
   ↓ build
dist/music_engine-4.0.0-py3-none-any.whl
   ↓
copias el wheel
   ↓
music-composer-lab/.vendor/
   ↓
pip install .vendor\music_engine-4.0.0-py3-none-any.whl
   ↓
music-midi funciona dentro del .venv del lab
```

No necesitas variable de entorno.

### Opción recomendada: vendor local del wheel

En `music-engine`:

```powershell
cd D:\projects\music-engine

python -m build --wheel

Get-ChildItem .\dist
```

Deberías obtener algo parecido a:

```text
music_engine-4.0.0-py3-none-any.whl
```

Luego en `music-composer-lab`:

```powershell
cd D:\projects\music-composer-lab

New-Item -ItemType Directory -Force .vendor

Copy-Item `
  D:\projects\music-engine\dist\music_engine-4.0.0-py3-none-any.whl `
  .\.vendor\
```

Y en el `.gitignore` del lab:

```gitignore
.vendor/
```

Así **el compilado existe localmente pero nunca entra al repositorio**.

Luego crea/activa el entorno del lab:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala el wheel:

```powershell
python -m pip install .\.vendor\music_engine-4.0.0-py3-none-any.whl
```

Y prueba:

```powershell
music-midi --help
```

Después:

```powershell
music-midi songplan --help
music-midi songplan validate --help
music-midi songplan render --help
```

Con eso ya estás usando **el ejecutable instalado desde el wheel**, no el source de:

```text
D:\projects\music-engine
```

### Incluso puedes verificar que no esté agarrando el repo

En PowerShell:

```powershell
Get-Command music-midi
```

Debería apuntar a algo similar a:

```text
D:\projects\music-composer-lab\.venv\Scripts\music-midi.exe
```

Y:

```powershell
python -c "import music_engine; print(music_engine.__file__)"
```

debería mostrar algo parecido a:

```text
D:\projects\music-composer-lab\.venv\Lib\site-packages\music_engine\__init__.py
```

Eso prueba que está usando el paquete instalado.

### Flujo de actualización mientras desarrollas

Cada vez que quieras probar una versión nueva del motor:

```text
music-engine
   ↓
python -m build --wheel
   ↓
copiar wheel nuevo
   ↓
pip install --force-reinstall wheel
```

Por ejemplo:

```powershell
python -m pip install --force-reinstall `
  .\.vendor\music_engine-4.0.0-py3-none-any.whl
```

Aunque la versión siga diciendo `4.0.0`, `--force-reinstall` obliga a reemplazar la instalación.

### Y para que Codex lo pueda usar

Yo pondría en `music-composer-lab` una convención simple:

```text
.vendor/
    music_engine-4.0.0-py3-none-any.whl
```

ignorada por Git, y documentaría:

```text
music-engine is an external runtime dependency.

For local development it is installed from a wheel into the project's .venv.

The wheel lives under `.vendor/` and MUST NOT be committed.
```

Así Codex puede ejecutar:

```powershell
music-midi songplan validate ...
music-midi songplan render ...
```

porque al trabajar dentro del `.venv` del lab el comando estará disponible normalmente.

No necesitas:

```text
PYTHONPATH
PATH manual
editable install
referencia al source de music-engine
```

Eso además es una prueba arquitectónica excelente: si `music-composer-lab` funciona teniendo únicamente el **wheel + contrato público**, significa que realmente está desacoplado de la implementación de `music-engine`.

## Project convention

`music-engine` is an external runtime dependency.

For local development, it is installed from a wheel into the project's `.venv`.

The wheel lives under `.vendor/` and MUST NOT be committed.

Codex must use the executable from:

`.venv/Scripts/music-midi.exe`

Codex must not depend on the source repository of `music-engine`.

If the required engine capability is unavailable through the public contract,
the experiment must report that limitation rather than modifying `music-engine`.
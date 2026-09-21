# Trazabilidad de payloads de Stage 1

La primera composición del payload se generó antes de detectar que la consola PowerShell había sustituido caracteres acentuados en el archivo español de capacidades host. Nunca se pasó al runner ni se transmitió. Su payload conservado tiene SHA256 `550c5eb9ea38385d54c799e4b10d14f8bedbc3674d048e807d521a5057855d4c`; su manifiesto quedó marcado `SUPERSEDED_DRAFT_NOT_EXECUTED` y con `preflight.pass: false`.

El input preparado final es `outputs/codex/stage-1/payload/revision-2/attempt-1-payload.txt`, que contiene el archivo UTF-8 corregido y pasó el preflight del assembler. Su SHA256 es `58646fd9fbef25c17b6b5cc7f846490989316f25d5084469d2b8b4cb074a423d`. No se sobrescribió silenciosamente el borrador ni se ejecutó Codex.

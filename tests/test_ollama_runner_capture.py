import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import subprocess
import tempfile
import threading
import unittest

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "integrations/composer-agent/ollama_runner.py"
SCHEMA = ROOT / "datasets/composer-interface-v1.1/output-schema.json"
VALIDATOR = ROOT / "integrations/composer-agent/validate_v1_1_output.py"


class Handler(BaseHTTPRequestHandler):
    response_bytes = b'{"model":"fixture","message":{"content":"\u00e1rbol \ud83c\udfb5"},"done":true}'

    def do_POST(self):
        self.server.request_body = self.rfile.read(int(self.headers["Content-Length"]))
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(self.response_bytes)

    def log_message(self, *_args):
        pass


class RunnerCaptureTest(unittest.TestCase):
    def test_utf8_raw_capture_metadata_and_overwrite_refusal(self):
        server = HTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as tmp:
                temp = Path(tmp)
                prompt = temp / "prompt.txt"
                brief = temp / "brief.yaml"
                out = temp / "model-out"
                prompt.write_text("prueba ñ", encoding="utf-8")
                brief.write_text("brief", encoding="utf-8")
                command = ["python", str(RUNNER), "--model", "fixture", "--input", str(prompt), "--brief", str(brief), "--output-dir", str(out), "--schema", str(SCHEMA), "--ollama-url", f"http://127.0.0.1:{server.server_port}/api/chat", "--num-predict", "12288"]
                first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                self.assertEqual(first.returncode, 0, first.stderr)
                raw = out / "raw-output.txt"
                api_raw = out / "raw-api-response.json"
                manifest = json.loads((out / "capture-manifest.json").read_text(encoding="utf-8"))
                self.assertEqual(raw.read_bytes(), "árbol 🎵".encode("utf-8"))
                self.assertEqual(api_raw.read_bytes(), Handler.response_bytes)
                self.assertEqual(manifest["raw_output_sha256"], hashlib.sha256(raw.read_bytes()).hexdigest())
                self.assertFalse(manifest["semantic_repair_performed"])
                payload = json.loads(server.request_body.decode("utf-8"))
                self.assertEqual(payload["options"]["temperature"], 0)
                self.assertEqual(payload["options"]["num_predict"], 12288)
                self.assertEqual(manifest["generation_parameters"]["num_predict"], 12288)
                original = raw.read_bytes()
                second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
                self.assertNotEqual(second.returncode, 0)
                self.assertEqual(raw.read_bytes(), original)
        finally:
            server.shutdown()
            server.server_close()

    def test_gate_rejects_ready_with_missing_decisions_without_rewriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            response = Path(tmp) / "raw-output.txt"
            original = b'{"status":"READY_FOR_VALIDATION","completion_checklist":[],"songplan_candidate":null}'
            response.write_bytes(original)
            result = subprocess.run(["python", str(VALIDATOR), str(response)], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("missing required checklist decisions", result.stdout)
            self.assertEqual(response.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()

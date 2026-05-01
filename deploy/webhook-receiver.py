#!/usr/bin/env python3
"""
Webhook receiver for MkDocs site deployment.

Usage:
    WEBHOOK_TOKEN=<secret> WEBHOOK_PORT=9000 python3 webhook-receiver.py

The token must match the DEPLOY_WEBHOOK_TOKEN secret set in GitHub Actions.
"""
import hmac
import json
import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

WEBHOOK_TOKEN = os.environ.get("WEBHOOK_TOKEN", "")
DEPLOY_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deploy.sh")

if not WEBHOOK_TOKEN:
    print("ERROR: WEBHOOK_TOKEN environment variable is not set", file=sys.stderr)
    sys.exit(1)


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        token = self.headers.get("X-Webhook-Token", "")
        if not hmac.compare_digest(token, WEBHOOK_TOKEN):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Forbidden")
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            payload = json.loads(body)
        except (json.JSONDecodeError, ValueError):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        download_url = payload.get("download_url", "")
        sha = payload.get("sha", "unknown")

        if not download_url:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing download_url")
            return

        self.send_response(202)
        self.end_headers()
        self.wfile.write(b"Accepted")

        subprocess.Popen(
            [DEPLOY_SCRIPT, download_url, sha],
            stdout=open("/var/log/mkdocs-deploy.log", "a"),
            stderr=subprocess.STDOUT,
            close_fds=True,
        )

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}", flush=True)


if __name__ == "__main__":
    port = int(os.environ.get("WEBHOOK_PORT", "9000"))
    server = HTTPServer(("127.0.0.1", port), WebhookHandler)
    print(f"Webhook receiver listening on 127.0.0.1:{port}", flush=True)
    server.serve_forever()

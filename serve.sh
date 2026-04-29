#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ ! -f venv/bin/mkdocs ]; then
  echo "ERROR: virtualenv not found. Run: python3 -m venv venv && venv/bin/pip install mkdocs-material"
  exit 1
fi

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"

echo "Starting MeshCore CSRA dev server at http://localhost:${PORT}"
echo "Press Ctrl+C to stop."
echo ""

exec venv/bin/mkdocs serve --dev-addr="${HOST}:${PORT}" --dirtyreload

#!/usr/bin/env bash
set -euo pipefail

DOWNLOAD_URL="${1:?Usage: deploy.sh <download_url> <sha>}"
SHA="${2:-unknown}"
DEPLOY_DIR="${DEPLOY_DIR:-/srv/csrameshcore}"
WORK_DIR="/tmp/mkdocs-deploy-$$"

log() { echo "[$(date -Iseconds)] $*"; }

log "Starting deploy of commit $SHA"
log "Download URL: $DOWNLOAD_URL"

mkdir -p "$WORK_DIR"
trap 'rm -rf "$WORK_DIR"' EXIT

log "Downloading site package..."
curl -fsSL -o "$WORK_DIR/site.tar.gz" "$DOWNLOAD_URL"

log "Extracting..."
mkdir -p "$WORK_DIR/site"
tar -xzf "$WORK_DIR/site.tar.gz" -C "$WORK_DIR/site"

log "Deploying to $DEPLOY_DIR..."
mkdir -p "$DEPLOY_DIR"
rsync -a --delete "$WORK_DIR/site/" "$DEPLOY_DIR/"

log "Deploy complete."

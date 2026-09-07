#!/usr/bin/env bash
# Levanta un server estático local con hot reload.
#
# Uso:  bash scripts/dev.sh [puerto]
# Abrí: http://localhost:<puerto>
#
# Con Node (npx): recarga al cambiar HTML/CSS/JS.
# Sin Node: cae a python3 -m http.server (sin reload).
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${1:-4177}"

if command -v npx >/dev/null 2>&1; then
  echo "Sirviendo con hot reload en http://localhost:$PORT (Ctrl+C para cortar)"
  exec npx --yes live-server . \
    --port="$PORT" \
    --host=127.0.0.1 \
    --no-browser \
    --wait=100 \
    --ignorePattern="(\\.git|\\.shots|node_modules|\\.claude|\\.cursor|\\.agents|\\.impeccable)"
fi

echo "npx no encontrado — sirviendo sin hot reload en http://localhost:$PORT"
echo "Instalá Node.js para hot reload."
exec python3 -m http.server "$PORT" --directory .

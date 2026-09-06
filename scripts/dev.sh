#!/usr/bin/env bash
# Levanta un server estático local para desarrollo.
#
# Uso:  bash scripts/dev.sh [puerto]
# Abrí: http://localhost:<puerto>
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${1:-4177}"

echo "Sirviendo en http://localhost:$PORT (Ctrl+C para cortar)"
exec python3 -m http.server "$PORT" --directory .

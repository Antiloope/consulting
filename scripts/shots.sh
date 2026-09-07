#!/usr/bin/env bash
# Capturas de la página en viewports reales de mobile y desktop.
#
# Chrome headless ignora <meta viewport> y maquetaría todo a 980px, así que
# scripts/viewport.html mete el sitio en un iframe del ancho pedido. Ese iframe
# sí le da a la página el viewport correcto.
#
# Uso:  bash scripts/shots.sh [puerto]
# Salida: .shots/*.png  (ignorado por git)
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${1:-4177}"
OUT=".shots"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

[ -x "$CHROME" ] || { echo "No encuentro Chrome en: $CHROME"; echo "Pasalo con CHROME=/ruta/a/chrome"; exit 1; }

if ! curl -sf -o /dev/null "http://127.0.0.1:$PORT/"; then
  echo "No hay nada sirviendo en el puerto $PORT."
  echo "Levantalo con: bash scripts/dev.sh $PORT"
  exit 1
fi

mkdir -p "$OUT"

# nombre  ancho  alto  scrollY  abrir-servicios
shot() {
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 \
    --window-size="$2,$3" --screenshot="$OUT/$1.png" \
    "http://127.0.0.1:$PORT/scripts/viewport.html?w=$2&h=$3&y=${4:-0}&open=${5:-}" 2>/dev/null
  echo "  $OUT/$1.png"
}

echo "Mobile (390x844):"
shot mobile-hero      390 844 0
shot mobile-senales   390 844 880
shot mobile-servicios 390 844 3550 1
shot mobile-caso      390 844 5100

echo "Desktop (1280x900):"
shot desktop-hero     1280 900 0
shot desktop-madurez  1280 900 2350
shot desktop-caso     1280 900 4450

echo "Listo."

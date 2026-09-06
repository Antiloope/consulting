#!/usr/bin/env bash
# Regenera assets/img/og.png y assets/img/apple-touch-icon.png desde sus
# fuentes SVG (scripts/og-image.svg, scripts/touch-icon.svg).
#
# Usa `qlmanage` (QuickLook, viene con macOS) para rasterizar y `sips` para
# recortar. Sin dependencias externas, pero solo corre en macOS.
#
# El truco del canvas cuadrado en og-image.svg no es opcional: ver el
# comentario en ese archivo antes de tocar sus dimensiones.
set -euo pipefail
cd "$(dirname "$0")/.."

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

echo "→ og.png (1200×630)"
qlmanage -t -s 1200 -o "$tmp" scripts/og-image.svg >/dev/null
sips -c 630 1200 --cropOffset 285 0 \
  "$tmp/og-image.svg.png" --out assets/img/og.png >/dev/null

echo "→ apple-touch-icon.png (180×180)"
qlmanage -t -s 180 -o "$tmp" scripts/touch-icon.svg >/dev/null
cp "$tmp/touch-icon.svg.png" assets/img/apple-touch-icon.png

echo "Listo. Revisá el resultado antes de hacer commit:"
echo "  open assets/img/og.png assets/img/apple-touch-icon.png"

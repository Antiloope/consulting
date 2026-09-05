#!/usr/bin/env bash
# Presupuesto de performance. Corré: bash scripts/size.sh
set -euo pipefail
cd "$(dirname "$0")/.."

printf '%-28s %10s %10s\n' ARCHIVO CRUDO GZIP
printf '%-28s %10s %10s\n' '---' '---' '---'

total_raw=0; total_gz=0
for f in index.html assets/css/*.css assets/js/*.js; do
  raw=$(wc -c < "$f")
  gz=$(gzip -9 -c "$f" | wc -c)
  total_raw=$((total_raw + raw)); total_gz=$((total_gz + gz))
  printf '%-28s %9dB %9dB\n' "$f" "$raw" "$gz"
done

printf '%-28s %10s %10s\n' '---' '---' '---'
printf '%-28s %8.1fKB %8.1fKB\n' TOTAL \
  "$(echo "$total_raw" | awk '{print $1/1024}')" \
  "$(echo "$total_gz" | awk '{print $1/1024}')"

budget=25600
if [ "$total_gz" -gt "$budget" ]; then
  echo; echo "FUERA DE PRESUPUESTO: $total_gz B gzip > $budget B"; exit 1
fi
echo; echo "Dentro del presupuesto (< 25 KB gzip)."

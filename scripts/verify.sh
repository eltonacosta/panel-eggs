#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if [[ ! -f SHA256SUMS ]]; then
  echo "SHA256SUMS não encontrado." >&2
  exit 1
fi

sha256sum -c SHA256SUMS

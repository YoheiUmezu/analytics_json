#!/bin/zsh
set -euo pipefail

cd "/Users/umedzuyouhei/Desktop/analytics"
source "venv/bin/activate"
python "generate_analytics.py"

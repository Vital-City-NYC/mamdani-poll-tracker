#!/bin/sh
# Re-shoot share.png (the 1200x630 social/search preview) from share.html.
# Needs the folder served locally, e.g. python3 -m http.server 8978 from the repo's parent,
# or pass a URL: ./share.sh http://localhost:8000/share.html
URL="${1:-http://localhost:8978/mamdani-poll-tracker/share.html}"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --window-size=1200,630 --force-device-scale-factor=1 --virtual-time-budget=8000 \
  --screenshot="$(dirname "$0")/share.png" "$URL"

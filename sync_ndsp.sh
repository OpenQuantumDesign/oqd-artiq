#!/bin/bash
# Sync NDSP files from submodule to artiq/
# Usage: ./sync_ndsp.sh

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

SRC="$REPO_ROOT/contrib/oqd-spectrum-ndsp/src/artiq"
DEST="$REPO_ROOT/artiq"

echo "Updating submodule..."
git submodule update --remote --merge contrib/oqd-spectrum-ndsp

echo "Syncing AWG driver files..."
cp -v "$SRC/devices/awg/"*.py "$DEST/devices/awg/"

echo "Syncing AWG frontend..."
cp -v "$SRC/frontend/aqctl_awg.py" "$DEST/frontend/"

echo "Done."

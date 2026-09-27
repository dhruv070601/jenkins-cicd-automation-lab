#!/usr/bin/env bash
set -euo pipefail
test -f Jenkinsfile
test -f README.md
echo "Validation passed."

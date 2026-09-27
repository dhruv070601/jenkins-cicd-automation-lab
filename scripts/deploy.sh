#!/usr/bin/env bash
set -euo pipefail
env="${1:-dev}"
tag="${2:-local}"
echo "Deployment simulation: environment=$env image=$tag"

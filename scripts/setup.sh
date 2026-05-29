#!/bin/bash
set -e

echo "Creating required folders..."
mkdir -p data/prometheus data/grafana logs screenshots

if [ ! -f .env ]; then
  echo "Creating .env from .env.example..."
  cp .env.example .env
else
  echo ".env already exists. Skipping copy."
fi

echo "Making scripts executable..."
chmod +x scripts/*.sh

echo "Setup complete. Edit .env if needed, then run ./scripts/start.sh"

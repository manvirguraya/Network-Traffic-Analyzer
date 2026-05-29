#!/bin/bash
set -e

echo "Starting Network Traffic Analyzer stack..."
docker compose up -d --build

echo "Services started."
docker compose ps

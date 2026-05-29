#!/bin/bash
set -e

echo "Stopping Network Traffic Analyzer stack..."
docker compose down

echo "Services stopped."

#!/bin/bash
set -e

echo "Checking containers..."
docker compose ps

echo ""
echo "Checking analyzer health endpoint..."
curl -f http://localhost:8000/health || true

echo ""
echo "Checking analyzer metrics endpoint..."
curl -f http://localhost:8000/metrics | head || true

echo ""
echo "Checking Prometheus..."
curl -I http://localhost:9090 || true

echo ""
echo "Checking Grafana..."
curl -I http://localhost:3000 || true

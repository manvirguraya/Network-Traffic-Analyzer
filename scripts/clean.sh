#!/bin/bash
set -e

echo "Stopping containers..."
docker compose down

echo "Removing unused Docker resources..."
docker system prune -f

echo "Cleanup complete. Persistent data folders were not deleted."

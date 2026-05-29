import os

INTERFACE = os.getenv("INTERFACE", "any")
METRICS_HOST = os.getenv("METRICS_HOST", "0.0.0.0")
METRICS_PORT = int(os.getenv("METRICS_PORT", "8000"))

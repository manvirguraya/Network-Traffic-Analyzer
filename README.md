# Network Traffic Analyzer & Monitoring Dashboard

A Linux-based network monitoring platform that captures, analyzes, and visualizes local network activity using Python, Scapy, Prometheus, Grafana, and Docker.

## Project Description

This project monitors network traffic on a Linux machine and exposes traffic metrics for visualization in Grafana. The analyzer captures packets, identifies protocols, tracks bandwidth usage, records source/destination activity, and exports metrics through a Prometheus-compatible endpoint.

## Features

- Real-time packet capture using Python and Scapy
- Protocol analysis for TCP, UDP, ICMP, DNS, HTTP, HTTPS, and other traffic
- Bandwidth monitoring for incoming and outgoing traffic
- Top source and destination IP tracking
- Prometheus metrics endpoint for monitoring
- Grafana dashboard for traffic visualization
- Dockerized deployment with Docker Compose
- Bash scripts for setup, startup, shutdown, health checks, and cleanup
- Optional host-network mode for Linux packet capture

## Technologies Used

- Python
- Scapy
- Flask
- Prometheus Client
- Docker
- Docker Compose
- Linux
- Bash
- Grafana
- Prometheus

## Architecture

```txt
Local Network Traffic
        |
        v
Python Packet Analyzer
        |
        v
Prometheus Metrics Endpoint (:8000/metrics)
        |
        v
Prometheus
        |
        v
Grafana Dashboard
```

## Repository Structure

```txt
network-traffic-analyzer/
|
|-- README.md
|-- docker-compose.yml
|-- Dockerfile
|-- requirements.txt
|-- .env.example
|-- .gitignore
|
|-- src/
|   |-- analyzer.py
|   |-- metrics.py
|   |-- config.py
|
|-- configs/
|   |-- prometheus/
|   |   |-- prometheus.yml
|   |
|   |-- grafana/
|       |-- provisioning/
|       |   |-- datasources/
|       |   |   |-- prometheus.yml
|       |   |-- dashboards/
|       |       |-- dashboard.yml
|       |-- dashboards/
|           |-- network-dashboard.json
|
|-- scripts/
|   |-- setup.sh
|   |-- start.sh
|   |-- stop.sh
|   |-- healthcheck.sh
|   |-- clean.sh
|
|-- docs/
|   |-- setup-guide.md
|   |-- troubleshooting.md
|   |-- resume-bullets.md
|
|-- data/
|   |-- .gitkeep
|-- logs/
|   |-- .gitkeep
|-- screenshots/
|   |-- .gitkeep
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/network-traffic-analyzer.git
cd network-traffic-analyzer
```

### 2. Create the Environment File

```bash
cp .env.example .env
```

Edit `.env` if needed:

```bash
nano .env
```

### 3. Make Scripts Executable

```bash
chmod +x scripts/*.sh
```

### 4. Start the Project

```bash
./scripts/start.sh
```

Or manually:

```bash
docker compose up -d --build
```

### 5. View Services

| Service | URL |
|---|---|
| Packet Analyzer Metrics | `http://localhost:8000/metrics` |
| Prometheus | `http://localhost:9090` |
| Grafana | `http://localhost:3000` |

Default Grafana login:

```txt
Username: admin
Password: admin
```

Change the password after logging in.

## How It Works

The Python analyzer uses Scapy to sniff packets from a selected network interface. It updates Prometheus metrics for packet counts, protocol usage, bandwidth, source IPs, and destination IPs. Prometheus scrapes those metrics from the analyzer, and Grafana visualizes them using a preloaded dashboard.

## Important Linux Permission Note

Packet capture requires elevated network permissions. This project runs the analyzer container with capabilities needed for packet sniffing:

```yaml
cap_add:
  - NET_ADMIN
  - NET_RAW
network_mode: host
```

This setup is intended for Linux machines such as Raspberry Pi OS, Ubuntu Server, Debian, or an old laptop running Linux.

## Useful Commands

Start services:

```bash
./scripts/start.sh
```

Stop services:

```bash
./scripts/stop.sh
```

Run health check:

```bash
./scripts/healthcheck.sh
```

View logs:

```bash
docker compose logs -f analyzer
```

Clean stopped containers and unused Docker resources:

```bash
./scripts/clean.sh
```

## Resume Summary

Built a Linux-based network traffic monitoring platform using Python, Scapy, Docker, Prometheus, and Grafana to capture, analyze, and visualize real-time network activity and bandwidth usage.

## Disclaimer

Only monitor networks that you own or have permission to analyze. Packet capture can expose sensitive metadata, so this project is intended for educational and personal network diagnostics only.

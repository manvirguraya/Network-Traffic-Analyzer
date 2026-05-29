# Network Traffic Analyzer & Monitoring Dashboard

A Linux-based network traffic monitoring platform that captures, analyzes, and visualizes real-time network activity using Python, Docker, Prometheus, and Grafana. This project can run on a Raspberry Pi, old laptop, desktop, mini PC, or Linux virtual machine.

The stack includes Python packet analysis tools for monitoring traffic, Prometheus for metrics collection, Grafana for visualization dashboards, Node Exporter and cAdvisor for host/container monitoring, and Docker Compose for deployment and orchestration.

---

# Project Description

This project demonstrates how network traffic and bandwidth usage can be monitored and analyzed using Linux networking tools, Python packet inspection, and containerized monitoring infrastructure. Docker Compose is used to deploy monitoring services while Python scripts capture and process network activity for visualization and diagnostics.

---

# Features

- Real-time network traffic monitoring and packet analysis
- Bandwidth usage visualization and analytics
- Protocol inspection using Python and Scapy
- Docker container monitoring with cAdvisor
- Host system monitoring with Node Exporter
- Metrics collection using Prometheus
- Interactive monitoring dashboards with Grafana
- Automated setup, updates, backups, and health checks using Bash scripts
- Environment variable template using `.env.example`
- Persistent monitoring data stored under `data/`

---

# Technologies Used

- Linux / Ubuntu Server / Raspberry Pi OS
- Python
- Scapy
- Docker
- Docker Compose
- Bash
- YAML
- Grafana
- Prometheus
- Node Exporter
- cAdvisor

---

# Architecture

```txt
Internet
   |
Router
   |
Linux Monitoring Server
   |-- Python Packet Analyzer
   |-- Network Traffic Monitoring
   |-- Prometheus Metrics Collection
   |-- Grafana Monitoring Dashboard
   |-- Node Exporter Host Metrics
   |-- cAdvisor Container Metrics
```

---

# Repository Structure

```txt
network-traffic-analyzer/
|
|-- README.md
|-- docker-compose.yml
|-- .env
|-- .env.example
|-- .gitignore
|
|-- src/
|   |-- analyzer.py
|   |-- exporter.py
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
|       |       |-- dashboards.yml
|       |
|       |-- dashboards/
|           |-- network-overview.json
|
|-- docs/
|   |-- setup.md
|   |-- troubleshooting.md
|
|-- scripts/
|   |-- install-docker.sh
|   |-- setup.sh
|   |-- start-services.sh
|   |-- stop-services.sh
|   |-- update-containers.sh
|   |-- backup.sh
|   |-- healthcheck.sh
|
|-- data/
|   |-- .gitkeep
|
|-- backups/
|   |-- .gitkeep
|
|-- screenshots/
|   |-- .gitkeep
```

---

# Setup Instructions

## 1. Prepare the Server

Install a Linux-based OS on your Raspberry Pi, old laptop, desktop, mini PC, or virtual machine.

Recommended options:

- Ubuntu Server
- Debian
- Raspberry Pi OS 64-bit
- Ubuntu Desktop if you want a GUI

Make sure the system has internet access.

---

## 2. Install Git

```bash
sudo apt update
sudo apt install git -y
```

---

## 3. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/network-traffic-analyzer.git
cd network-traffic-analyzer
```

---

## 4. Install Docker

```bash
chmod +x scripts/*.sh
./scripts/install-docker.sh
```

After Docker installs, reboot or log out and back in:

```bash
sudo reboot
```

Then return to the project folder.

---

## 5. Run Project Setup

```bash
./scripts/setup.sh
```

This script:

- creates required folders
- copies `.env.example` to `.env`
- validates the Docker Compose file
- prepares the monitoring environment

---

## 6. Edit Environment Variables

```bash
nano .env
```

Change the default values before starting services.

Example:

```env
TZ=America/Chicago
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=change_this_password
NETWORK_INTERFACE=eth0
```

---

## 7. Start the Monitoring Services

```bash
./scripts/start-services.sh
```

This runs:

```bash
docker compose up -d
```

Docker will download and start:

- Grafana
- Prometheus
- Node Exporter
- cAdvisor

---

## 8. Start the Python Network Analyzer

The analyzer may require elevated permissions to inspect network packets:

```bash
sudo python3 src/analyzer.py
```

If the project uses a Prometheus exporter, run:

```bash
sudo python3 src/exporter.py
```

---

## 9. Check Running Containers

```bash
docker compose ps
```

Or run:

```bash
./scripts/healthcheck.sh
```

---

# Service URLs

Replace `SERVER-IP` with your device's local IP address.

| Service | URL |
|---|---|
| Grafana | `http://SERVER-IP:3000` |
| Prometheus | `http://SERVER-IP:9090` |
| cAdvisor | `http://SERVER-IP:8081` |

---

# Default Logins

## Grafana

Username and password come from your `.env` file:

```env
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=change_this_password
```

---

# Useful Commands

## Start services

```bash
./scripts/start-services.sh
```

## Stop services

```bash
./scripts/stop-services.sh
```

## View logs

```bash
docker compose logs -f
```

## Update containers

```bash
./scripts/update-containers.sh
```

## Run health check

```bash
./scripts/healthcheck.sh
```

## Run backup

```bash
./scripts/backup.sh
```

## Run packet analyzer

```bash
sudo python3 src/analyzer.py
```

## Run Prometheus exporter

```bash
sudo python3 src/exporter.py
```

---

# Grafana Monitoring Setup

Grafana is automatically provisioned with Prometheus as a data source and includes starter dashboards for:

- network traffic metrics
- bandwidth monitoring
- Docker container statistics
- Linux host monitoring

Prometheus collects metrics from:

- Prometheus itself
- Node Exporter for host system metrics
- cAdvisor for Docker container metrics
- Python monitoring exporter for network traffic metrics

---

# Packet Analysis

The Python analyzer uses Scapy to inspect network packets and collect traffic statistics.

Example traffic types:

- TCP
- UDP
- DNS
- HTTP
- ICMP

The analyzer can be extended to track:

- packet counts
- bandwidth usage
- source and destination IPs
- protocol distribution
- traffic spikes
- suspicious network activity

---

## Disclaimer

Only monitor networks that you own or have permission to analyze. Packet capture can expose sensitive metadata, so this project is intended for educational and personal network diagnostics only.

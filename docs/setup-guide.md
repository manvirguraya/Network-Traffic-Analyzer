# Setup Guide

## 1. Install Docker

On Ubuntu, Debian, or Raspberry Pi OS:

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

Log out and back in after adding your user to the Docker group.

## 2. Clone and Configure

```bash
git clone https://github.com/YOUR-USERNAME/network-traffic-analyzer.git
cd network-traffic-analyzer
cp .env.example .env
chmod +x scripts/*.sh
```

## 3. Choose Network Interface

Find interfaces:

```bash
ip addr
```

Common names:

```txt
eth0   Ethernet
wlan0  Wi-Fi
any    All interfaces where supported
```

Edit `.env`:

```env
INTERFACE=any
```

## 4. Start

```bash
./scripts/start.sh
```

## 5. Open Dashboards

- Analyzer metrics: `http://localhost:8000/metrics`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

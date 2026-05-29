# Troubleshooting

## Analyzer starts but no traffic appears

Try changing the interface in `.env`:

```env
INTERFACE=eth0
```

or:

```env
INTERFACE=wlan0
```

Then restart:

```bash
docker compose down
docker compose up -d --build
```

## Permission errors during packet capture

Packet sniffing requires Linux network capabilities. Confirm the analyzer service has:

```yaml
cap_add:
  - NET_ADMIN
  - NET_RAW
network_mode: host
```

## Grafana does not show data

Check Prometheus targets:

```txt
http://localhost:9090/targets
```

The `network-analyzer` target should be UP.

## Port already in use

Check which process is using a port:

```bash
sudo lsof -i :3000
sudo lsof -i :8000
sudo lsof -i :9090
```

Stop the conflicting service or change the port.

## Docker command permission denied

Run:

```bash
sudo usermod -aG docker $USER
```

Then log out and back in.

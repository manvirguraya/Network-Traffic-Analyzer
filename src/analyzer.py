import logging
import threading
from flask import Flask, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS

from src.config import INTERFACE, METRICS_HOST, METRICS_PORT
from src.metrics import (
    PACKETS_TOTAL,
    BYTES_TOTAL,
    SOURCE_IP_PACKETS,
    DESTINATION_IP_PACKETS,
    ACTIVE_CAPTURE,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

app = Flask(__name__)


def detect_protocol(packet) -> str:
    if packet.haslayer(DNS):
        return "DNS"
    if packet.haslayer(TCP):
        sport = int(packet[TCP].sport)
        dport = int(packet[TCP].dport)
        if sport == 80 or dport == 80:
            return "HTTP"
        if sport == 443 or dport == 443:
            return "HTTPS"
        return "TCP"
    if packet.haslayer(UDP):
        return "UDP"
    if packet.haslayer(ICMP):
        return "ICMP"
    return "OTHER"


def handle_packet(packet) -> None:
    protocol = detect_protocol(packet)
    packet_size = len(packet)

    PACKETS_TOTAL.labels(protocol=protocol).inc()
    BYTES_TOTAL.labels(protocol=protocol).inc(packet_size)

    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        SOURCE_IP_PACKETS.labels(source_ip=source_ip).inc()
        DESTINATION_IP_PACKETS.labels(destination_ip=destination_ip).inc()


def start_sniffer() -> None:
    logging.info("Starting packet capture on interface: %s", INTERFACE)
    ACTIVE_CAPTURE.set(1)
    try:
        sniff(iface=INTERFACE, prn=handle_packet, store=False)
    except Exception as exc:
        ACTIVE_CAPTURE.set(0)
        logging.exception("Packet capture failed: %s", exc)


@app.route("/")
def index() -> str:
    return "Network Traffic Analyzer is running. Metrics are available at /metrics."


@app.route("/health")
def health() -> dict:
    return {"status": "ok", "interface": INTERFACE}


@app.route("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def main() -> None:
    sniffer_thread = threading.Thread(target=start_sniffer, daemon=True)
    sniffer_thread.start()

    logging.info("Starting metrics server on %s:%s", METRICS_HOST, METRICS_PORT)
    app.run(host=METRICS_HOST, port=METRICS_PORT)


if __name__ == "__main__":
    main()

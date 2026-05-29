from prometheus_client import Counter, Gauge

PACKETS_TOTAL = Counter(
    "network_packets_total",
    "Total packets captured by protocol",
    ["protocol"],
)

BYTES_TOTAL = Counter(
    "network_bytes_total",
    "Total bytes captured by protocol",
    ["protocol"],
)

SOURCE_IP_PACKETS = Counter(
    "network_source_ip_packets_total",
    "Total packets grouped by source IP",
    ["source_ip"],
)

DESTINATION_IP_PACKETS = Counter(
    "network_destination_ip_packets_total",
    "Total packets grouped by destination IP",
    ["destination_ip"],
)

ACTIVE_CAPTURE = Gauge(
    "network_capture_active",
    "Whether packet capture is currently running. 1 means active, 0 means inactive.",
)

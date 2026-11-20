import time
from prometheus_client import start_http_server, Gauge

DELIVERY_TIME = Gauge('delivery_processing_seconds', 'Time spent processing delivery')

def get_metric_value():
    return 42.5

if __name__ == '__main__':
    start_http_server(8000)
    print("Metrics exporter running on port 8000...")
    while True:
        DELIVERY_TIME.set(get_metric_value())
        time.sleep(5)

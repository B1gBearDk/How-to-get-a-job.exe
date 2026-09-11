import psutil
import time
import logging

logging.basicConfig(
    filename="/var/log/cpu-monitor.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)

while True: 
    cpu = psutil.cpu_percent(interval=1)
    logging.info(cpu)
    time.sleep(5)



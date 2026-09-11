# CPU Monitor

A lightweight Linux system monitoring daemon: polls CPU utilization every 5 seconds using `psutil` and writes structured, timestamped log entries — the kind of always-on monitoring loop that feeds into a SIEM or alerting pipeline.

### What it demonstrates
- Writing long-running monitoring processes meant to run unattended
- Structured logging with consistent timestamp formatting (ISO 8601, UTC) — the same discipline that matters for correlating logs across systems in a SOC
- Basic system-resource instrumentation

### Run it
```bash
pip install psutil
python3 cpu-monitor.py
# logs to /var/log/cpu-monitor.log
```

### Log output
Excerpt (full run in [`cpu-monitor.log`](./cpu-monitor.log)):
```
2026-02-15T11:15:58Z INFO: 0.5
2026-02-15T11:16:04Z INFO: 1.8
2026-02-15T11:16:10Z INFO: 0.3
2026-02-15T11:16:16Z INFO: 0.8
```

Group coursework project from Scripting & Automation, BSc Cyber Security, Erhvervsakademi København (EK/KEA).

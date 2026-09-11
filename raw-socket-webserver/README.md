# Raw-Socket HTTP Server

A minimal HTTP/1.1 server written directly on top of Python's `socket` module — no `http.server`, no framework. Built to understand what an HTTP server actually does at the TCP/socket level: accept a connection, read the raw request bytes, and hand-construct a valid HTTP response.

Also implements custom access logging in Apache Combined Log Format style (`access.log` is the full log from a run).

### What it demonstrates
- Understanding of TCP sockets and the HTTP protocol below the framework layer
- Parsing raw request data and constructing valid HTTP responses by hand
- Structured logging of every request (IP, timestamp, request line, status, response size)

### Run it
```bash
python3 webserver.py
# serves on http://localhost:80 (requires root/admin to bind port 80)
```

### Log output
Full access log in [`access.log`](./access.log):
```
127.0.0.1 -- -- [15/Feb/2026:15:20:13 +0000] "GET / HTTP/1.1" 200 111
127.0.0.1 -- -- [15/Feb/2026:15:21:05 +0000] "GET / HTTP/1.1" 200 111
127.0.0.1 -- -- [15/Feb/2026:15:22:14 +0000] "HEAD / HTTP/1.1" 200 111
```

### Demo
[`Demo.mp4`](./Demo.mp4) — screen recording of the server handling requests.

Group coursework project from Scripting & Automation, BSc Cyber Security, Erhvervsakademi København (EK/KEA).

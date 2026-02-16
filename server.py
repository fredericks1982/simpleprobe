import os
from http.server import HTTPServer, BaseHTTPRequestHandler

SIMPLEPROBE_PORT = int(os.environ.get("SIMPLEPROBE_PORT", 9090))

HTML = """\
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Simple Probe</title></head>
<body><h1>Hello World</h1></body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(HTML.encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", SIMPLEPROBE_PORT), Handler)
    print(f"Probe running on port {SIMPLEPROBE_PORT}")
    server.serve_forever()

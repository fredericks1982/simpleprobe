import os
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 1982))

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
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Probe running on port {PORT}")
    server.serve_forever()

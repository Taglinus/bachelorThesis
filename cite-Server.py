import http.server
import socketserver
import os

PORT = 8000
FILE_TO_SERVE = "citations.txt"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == f"/{FILE_TO_SERVE}":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            with open(FILE_TO_SERVE, "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404, "File not found.")

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}. Access your file at http://localhost:{PORT}/{FILE_TO_SERVE}")
    httpd.serve_forever()

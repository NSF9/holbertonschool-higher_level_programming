#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class my_api(BaseHTTPRequestHandler):
    """
    A simple HTTP API handler that responds to GET requests
    on multiple endpoints: /, /data, /status.
    """

    def do_GET(self):
        """
        Handle GET requests for various endpoints and return appropriate response.
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """
    Initialize and run the HTTP server on localhost:8000.
    """
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, my_api)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

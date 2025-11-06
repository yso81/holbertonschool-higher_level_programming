#!/usr/bin/python3
"""
Basic HTTP Server
"""
import http.server
import socketserver
import json


PORT = 8000

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/data":

            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf-8"))

        elif self.path == "/info":
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info_data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_info, "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", "utf-8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port", PORT)
    print(f"- Visit http://localhost:{PORT}/ for the plain text API.")
    print(f"- Visit http://localhost:{PORT}/data for the JSON data.")
    print(f"- Visit http://localhost:{PORT}/info for the API info JSON data.")
    print(f"- Visit http://localhost:{PORT}/undefined for a 404 Not Found response.")

    httpd.serve_forever()

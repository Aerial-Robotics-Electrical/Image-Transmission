import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
# TODO write own handler for REST API requests

with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    print("launched server", PORT)
    httpd.serve_forever()

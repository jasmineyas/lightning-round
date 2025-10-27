#!/usr/bin/env python3
"""
Simple HTTP server to run Lightning Round app.
Usage: python3 serve.py
"""
import http.server
import socketserver
import socket
import os

PORT = 8001


class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow loading local files
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()


os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to an external address (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()

    print("\n⚡ ⚡ ⚡ Lightning Round is running! ⚡ ⚡ ⚡ ")
    print(f"\nOn this computer: http://localhost:{PORT}")
    print(f"On your phone (same WiFi): http://{local_ip}:{PORT}")
    print("Make sure your phone and computer are on the same WiFi network")
    print("\nConfig file: config.json (or config.example.json as fallback)")
    print("\nPress Ctrl+C to stop the server\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped")

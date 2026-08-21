#!/usr/bin/env python3
"""
serve.py — tiny static dev server for Arch Linux WebTTY.

Serves the repo over HTTP so the multi-file catalog (index.html + games.css +
games-data.js + games-noicon.js) loads exactly as it does on the deployed
githack site — relative paths and correct MIME types. `file://` works too, but
this mirrors production and enables things browsers gate behind http(s).

Usage:
    python3 tools/serve.py [port]      # default 8000
    then open http://localhost:8000/
"""

import http.server
import os
import socketserver
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".css": "text/css",
        ".webmanifest": "application/manifest+json",
    }

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s - %s\n" % (self.address_string(), fmt % args))


def main():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Arch Linux WebTTY dev server")
        print("  serving %s" % ROOT)
        print("  http://localhost:%d/   (Ctrl+C to stop)" % PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nstopped")


if __name__ == "__main__":
    main()

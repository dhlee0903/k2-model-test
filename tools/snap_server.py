import http.server, base64, sys, os
OUT = sys.argv[1]
class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        n = int(self.headers['Content-Length']); data = self.rfile.read(n).decode()
        name = self.path.strip('/') or 'snap'
        open(os.path.join(OUT, name + '.png'), 'wb').write(base64.b64decode(data.split(',')[1]))
        self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
http.server.ThreadingHTTPServer(('127.0.0.1', 8766), H).serve_forever()

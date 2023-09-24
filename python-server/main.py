from http.server import BaseHTTPRequestHandler, HTTPServer
import os
  
class UnchainedServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            static_folder = 'static'
            filename = os.path.join(static_folder, 'index.html')
            if os.path.isfile(filename):
                    with open(filename, 'rb') as file:
                        content = file.read()
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        self.wfile.write(content)
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write('<h2>Error: Try again later.<h2>'.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write('<h1>404 PAGE NOT FOUND <h1>'.encode())
try:
    port = HTTPServer(('', 8080), UnchainedServer)
    print("Serving at port: 8080...")
    port.serve_forever()
except KeyboardInterrupt:
    print("Server stopped")

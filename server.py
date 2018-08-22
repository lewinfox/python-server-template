
#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from mimetypes import types_map
import os
import json

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        print('GET request received to {} from {}'.format(self.path, self.client_address))
        parsed_url = urlparse(self.path)
        print('PARSED_URL: {}'.format(parsed_url))
        # If the route is "/", serve the main page and related resources. If the
        # route is "/data/", run the db query and return the results
        if parsed_url.path == "/":
            self.path = "/index.html"

        print('Serving page {}'.format(self.path))
        # Parse content type of request
        filename, extension = os.path.splitext(self.path)
        mimetype = types_map.get(extension)
        try:
            f = open(os.curdir + os.sep + self.path)
            self.send_response(200)
            self.send_header('Content-Type', mimetype)
            self.end_headers()
            self.wfile.write(bytes(f.read(), 'utf-8'))
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes('No dice, son', 'utf-8'))


    def do_POST(self):
        print('POST request received to {}'.format(self.path))
        print('PATH: {}'.format(self.path))

        print(self.headers)
        content_len = int(self.headers.get('Content-Length'))
        payload = json.loads(str(self.rfile.read(content_len), 'utf-8'))
        print('Payload:')
        print(payload)

        # Send headers
        self.send_response(200)
        self.end_headers()

        # Send content
        try:
            content  = json.dumps(payload).encode(encoding='utf_8')
            print(type(content))
            self.wfile.write(content)
        except Exception as e:
            print('Exception: {}'.format(e))

if __name__ == '__main__':
    print('Running server.py')

    hostname = 'localhost'
    port = 8000

    httpd = HTTPServer((hostname, port), RequestHandlerClass=MyServer)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()

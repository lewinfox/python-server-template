from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from mimetypes import types_map
import os
import json

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        print('GET request received to {} from {}'.format(self.path, self.client_address))
        parsed_url = urlparse(self.path)
        # If the route is "/", serve the main page and related resources. If the
        # route is "/data/", run the db query and return the results
        if parsed_url.path == "/":
            self.path = "/index.html"
            self.serve_page()
        elif parsed_url.path == "/data":
            self.serve_data()
        else:
            self.serve_page()


    def do_POST(self):
        print('POST request received to {}'.format(self.path))
        # TODO: Return some kind of 500 code

    def serve_page(self):
        """Respond to a request to '/'"""

        print('Serving page')
        # Parse content type of request
        filename, extension = os.path.splitext(self.path)
        mimetype = types_map[extension]
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

        return

    def serve_data(self):
        # Can't figure out extracting parameters from the request. Using a static
        # object to test JSON conversion.
        response = {
            "text": "This is the server speaking",
            "param1": 10,
            "param2": "This is static data"
        }
        response_json = json.dumps(response)

        # print('Serving data')
        # print('PATH: {}'.format(self.path))
        # query = urlparse(self.path).query
        # print('QUERY: {}'.format(query))
        # params = {x[0]: x[1] for x in [x.split("=") for x in query.split("&")]}
        # print('PARAMS: {}'.format(params))
        # params_json = json.dumps(params)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        # self.wfile.write(bytes(params_json, 'utf-8'))
        self.wfile.write(bytes(response_json, 'utf-8'))
        return

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

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):

        print('GET request received to {} from {}'.format(self.path, self.client_address))
        parsed_url = urlparse(self.path)
        # If the route is "/", serve the main page and related resources. If the
        # route is "/data/", run the db query and return the results
        if parsed_url.path == "/":
            self.serve_page()
        elif parsed_url.path == "/data":
            self.serve_data()


    def do_POST(self):
        print('POST request received to {}'.format(self.path))
        # TODO: Return some kind of 500 code

    def serve_page(self, parsed_url.query):
        print('Serving page')
        return

    def serve_data(self):
        print('Serving data')
        query = urlparse(self.path).query
        params = {x[0]: x[1] for x in [x.split("=") for x in query.split("&")]}
        print('PARAMS: {}'.format(params))
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

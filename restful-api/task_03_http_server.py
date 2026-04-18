leAPIHandler(BaseHTTPRequestHandler):

   def do_GET(self):
        """Handle GET requests"""

       if sel.path == "/":
            self.send_response(200)
            selader("Content-type", "text/plain")
            self.end_heaers()
           self.wfile.wrte(b"Hello, this is a simple API!")

f.send_respose(200)
            self.send_header"Content-type", "application/json")
            self.end_headers(

           data = {
                "name": "John",
                "age": 30,
               "city": "New York
            }
            self.wfile.write(json.dumps(data).encode())
        self.send_header("Content-type", "appli
wfile.write(json.umps("OK").encode())

        else:
            self.send_response(404)            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found\nEndpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start server"
    server_address = ("", port)    httpd = server_class(server_address, handler_class)
)

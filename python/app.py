from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(200)
       self.send_header('Content-type', 'text/plain')
       self.end_headers()
       self.wfile.write(b'Hello, World!')

def run(server_class=HTTPServer, handler_class=MyHandler):
   server_address = ('', 8000)
   httpd = server_class(server_address, handler_class)
   httpd.serve_forever()

if __name__ == "__main__":
   run()

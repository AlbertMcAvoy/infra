import json
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health/' or self.path == "/health":
            self.handle_health()
        elif self.path == '/get/' or self.path == '/get':
            self.handle_get()
        else:
            self.send_error(404)

    def do_POST(self):
       if self.path == '/add/' or self.path == '/add':
           self.handle_add()
       else:
           self.send_error(404)


    def headers():
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def handle_health(self):
        self.headers()
        health_check = {"status": "OK"}
        self.wfile.write(json.dumps(health_check).encode('utf8'))

    def handle_get(self):
        self.headers()
        cnx = mysql.connector.connect(user='userIterator', password='qwerty1234', host='mariadb', database='iterator-db')
        cursor = cnx.cursor()
        query = ("SELECT * FROM interator")
        cursor.execute(query)
        iterators = []
        for (state) in cursor:
            entry = {"state": state}
            iterators.append(entry)
        response = {"status": "ok", "iterators": iterators}
        self.wfile.write(json.dumps(response).encode('utf8'))
        cursor.close()
        cnx.close()

    def handle_add(self):
        self.headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        value = data['value']
        cnx = mysql.connector.connect(user='userIterator', password='qwerty1234', host='mariadb', database='iterator-db')
        cursor = cnx.cursor()
        query = ("INSERT INTO interator (state) VALUES (%s)")
        cursor.execute(query, (value,))
        cnx.commit()
        response = {"status": "ok", "message": "Iterator value added successfully"}
        self.wfile.write(json.dumps(response).encode('utf8'))
        cursor.close()
        cnx.close()

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
   run()

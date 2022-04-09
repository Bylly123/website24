import http.server
from pickle import GET
import socketserver
import time

currenttime = time.strftime("%H:%M:%S")

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'c:/Users/Milo/Desktop/pywebserver/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 80
hostName = "bylly01.ddnss.org"

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("server started Completely http://%s:%s" % (hostName, PORT))
    try:
        print(currenttime)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("Server got close")
    print("Server started at:")
    print(currenttime)
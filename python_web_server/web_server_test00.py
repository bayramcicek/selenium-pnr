#!/usr/bin/python3.6
# created by cicek on 13.09.2019 16:22

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost', 4443), BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="./key.pem",
                               certfile='./cert.pem', server_side=True)

httpd.serve_forever()


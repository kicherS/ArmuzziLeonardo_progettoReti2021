#!/usr/bin/env python3
import sys, os, socket
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer
__file__='index.html'
HOST = socket.gethostname()

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

'''
Crea la porta di default 8080
'''
if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8080

'''
Recupera la Path della directory dove viene eseguito lo scrip e il file di homepage
'''
CWD = os.path.dirname(os.path.abspath(__file__))

server = ThreadingSimpleServer(('0.0.0.0', PORT), SimpleHTTPRequestHandler)
print("Serving HTTP traffic from", CWD, "on", HOST, "using port", PORT)




try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down...")
    server.socket.close()




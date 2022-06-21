#py4 protocol tunnelling
from http.server import BaseHTTPRequestHandler, HTTPServer
from base64 import b64encode, b64decode

class C2Server(BaseHTTPRequestHandler):
    def do_GET(self):
        #parsing headers
        data= b64decode( self.headers["Cookie"]).decode('utf-8').rstrip()
        print('Recieved %s' %data)
        if data=='secret data':
            response= b64encode( bytes('received', 'utf-8'))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_error(404)

if __name__=='__main__':
    hostname= 'localhost'
    port= 8443
    webServer= HTTPServer( (hostname, port), C2Server)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
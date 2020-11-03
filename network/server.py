from socketserver import BaseRequestHandler, UDPServer


class MyUDPServer(BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print('//wrote: {}'.format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    host, port = 'localhost', 8888
    with UDPServer((host, port), MyUDPServer) as s:
        s.serve_forever()



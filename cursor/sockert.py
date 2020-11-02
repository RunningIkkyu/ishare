import socket


class Server():
    def __init__(self):
        s = socket.socket()
        host = socket.gethostbyname()
        # use port 12223 to send data.
        port = 12223
        s.bind((host, port))
        s.listen(5)

    def send()


while True:
    c, add = s.accept()
    print("conn addr: " addr)
    c.send('hahahah')


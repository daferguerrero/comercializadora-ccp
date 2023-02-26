import socket

class Monitor:
    def ping(self):
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect(('127.0.0.1',5001))
            s.shutdown(2)
            return 'true'
        except:
            return 'false'
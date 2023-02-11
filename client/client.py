import socket

class Client():

    def __init__(self, host, port):
        self._host: str = host
        self._port: int = port

    def connect(self, message: bytes):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(message)
            data = sock.recv(1024).decode("utf-8")
        return data

    @property
    def host(self):
        return self._host
    
    @property
    def port(self):
        return self._port
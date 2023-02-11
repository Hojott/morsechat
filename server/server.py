import socket
import threading

class Server():

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

        self._users: list = []

    def create_socket(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((self.host, self.port))
        self.sock.listen()

    def stop_socket(self):
        self.sock.close()

    def restart(self):
        self.stop_socket()
        self.create_socket()

    def listen(self):
        while True:
            conn, addr = self.sock.accept()
            self.users.append(addr)
            with conn:
                print(f"Connection received: {addr}")
                self.create_thread(conn)

    def create_thread(self, conn: socket.socket):
        thread = threading.Thread(target=self.transmitter, args=(conn,))
        thread.start()

    def transmitter(self, conn: socket.socket):
        while True:
            message = conn.recv(1024)
            if not message:
                self.users.remove(conn.getpeername())
                break
            conn.sendall(message)

    def __enter__(self):
        self.create_socket()
        return self

    def __exit__(self, *args):
        self.stop_socket()

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def users(self) -> list:
        return self._users

    @property
    def sock(self) -> socket.socket:
        return self._sock

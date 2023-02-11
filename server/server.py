import time
import socket, threading
from connection import Connection

class Server():

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

        self._users: list = []
        self._messages: list = []

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
            registered = False
            for user, id in reversed(self.users):
                if addr == user.addr:
                    registered = True
                    print(f"Connection from {addr} as {id}")
                    user_conn: Connection = user
                    break

            if not registered:
                id = len(self.users) # len nicely outputs the next available id
                user_conn = Connection(id, conn, addr)
                self.users.append(user_conn)
                print(f"New connection from {addr} as {id}")

            self.create_thread(user_conn)

    def create_thread(self, conn: Connection):
        thread = threading.Thread(target=self.conn_listener, args=(conn,), name=conn.id)
        thread.start()

    def conn_listener(self, conn: Connection):
        while True:
            self.transmit_unread(conn)

            message = conn.receive()
            if not message:
                break
            self.messages.append(message)

    def transmit_unread(self, conn: Connection):
        for message in reversed(self.messages):
            message_timestamp: float = message[1]

            if conn.lastseen < message_timestamp:
                conn.unread[:0] = [message]

        conn.transmit_unread()
        conn.lastseen = time.time()

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
    def messages(self) -> list:
        return self._messages

    @property
    def sock(self) -> socket.socket:
        return self._sock

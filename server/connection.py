import socket
import time

class Connection():

    def __init__(self, id: int, conn: socket.socket, addr: tuple):
        self._id = id
        self._conn = conn
        self._addr = addr

        self._lastseen = time.time()
        self._unread = []

    def receive(self) -> bool:
        """ Server receives message from client
        """
        message = self.conn.recv(1024)
        timestamp = time.time()

        return (self.id, timestamp, message)

    def transmit(self, messages: list):
        """ Server transmits messages to client
        """
        for message in messages:
            id = str(message[0]).encode("utf-8")
            text = message[2]

            self.conn.sendall(text)

    def transmit_unread(self):
        """ Server transmits unread messages to client
        """
        self.transmit(self.unread)


    @property
    def id(self) -> int:
        return self._id

    @property
    def conn(self) -> socket.socket:
        return self._conn
    
    @property
    def addr(self) -> tuple:
        return self._addr

    @property
    def lastseen(self) -> float:
        return self._lastseen
    
    @lastseen.setter
    def lastseen(self, timestamp: float):
        if round(timestamp) != round(time.time()):
            raise ValueError("Timestamp is invalid!")
        else:
            self._lastseen = timestamp

    @property
    def unread(self) -> list:
        return self._unread

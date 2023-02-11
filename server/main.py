#!/usr/bin/env python3
from server import Server

if __name__ == '__main__':
    with Server('0.0.0.0', 5000) as server:
        server.listen()
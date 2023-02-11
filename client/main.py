#!/usr/bin/env python3
from client import Client

if __name__ == '__main__':
    input = input("-- ... --.: ").encode("utf-8")

    client = Client('0.0.0.0', 5000)
    print(client.connect(input))
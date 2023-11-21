import random
import socket

__doc__ = """Let's create simple network server and client.
This is client part.
"""

with socket.create_connection(('127.0.0.1', 10001)) as sock:
    n = random.randint(1, 100)
    sock.sendall(str(n).encode())
    print(f"Sent: {n}")
    received = sock.recv(1024)
    decoded = received.decode()
    print(f'Received: {decoded}')

import socket

__doc__ = """Let's create simple network server and client.
This is client part.
"""


with socket.create_connection(('127.0.0.1', 10001)) as sock:
    sock.sendall(b'10')
    print("Sent: 10")
    received = sock.recv(1024)
    decoded = received.decode()
    print(f'Received: {decoded}')

import socket
import sys
import threading

__doc__ = """Let's create simple TCP server and client.
Assume our server accept integers and return their squares.

def square_server(host, port) works well but with only one client.
It can be solved by using threading or multiprocessing.
Let's try Threads for the first approach.


square_server_threaded() works with multiple clients using polling approach.
It's not the best solution, because cycle is busy waiting for new connections.
There's a technique called "select" which allows to wait for multiple events.
Different OS have different implementations of "select" (*nix systems have POSIX select(), Windows has IOCP, etc.)
Python has unified API for all of them in selectors module.
"""


def handle_client(conn, addr):
    """
    Handle client connection
    """
    with conn:
        print(f'Connected by {addr}')
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    print(f'Connection closed by {addr}')
                    break

                try:
                    number = int(data.decode())
                    print(f'Received: {number}')
                except ValueError:
                    conn.sendall(b'Wrong input')

                try:
                    result = str(number ** 2).encode()
                    print(f'Result: {result.decode()}')
                except OverflowError:
                    conn.sendall(b'Overflow')
                except Exception as e:
                    conn.sendall(str(e).encode())

                print(f'Sending: {result.decode()}')
                conn.send(result)
            except ConnectionResetError:
                print(f'Connection reset by {addr}')
                break


def square_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        print(f'Server is listening on {host}:{port}')
        while True:
            conn, addr = sock.accept()
            handle_client(conn, addr)


def square_server_threaded(host, port):
    """
    On every connection create and start new thread
    Note Pyhon threading is not real threading even its API is similar to Java threads
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        print(f'Server is listening on {host}:{port}')
        while True:
            conn, addr = sock.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == '__main__':
    """
    Choose one of servers accepting connections host:port and run it
    """
    function = sys.argv[1]
    try:
        globals()[function]('127.0.0.1', 10001)
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")

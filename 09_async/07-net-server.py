import socket
import sys
import threading

__doc__ = """Let's create simple TCP server and client.
Assume our server accept integers and return their squares.

def square_server(host, port) works well but with only one client.
It can be solved by using threading or multiprocessing.
Let's try Threads for the first approach.
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

                print(f'Received: {data.decode()}')

                try:
                    number = int(data)
                    print(f'Number: {number}')
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
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen()
        print(f'Server is listening on {host}:{port}')
        while True:
            conn, addr = sock.accept()
            with conn:
                print(f'Connected by {addr}')
                threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == '__main__':
    """
    Choose one of servers accepting connections host:port and run it
    """
    function = sys.argv[1]
    try:
        locals()[function]('127.0.0.1', 10001)
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")

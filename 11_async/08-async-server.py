import signal
import socket
import sys
import selectors

__doc__ = """
There's a technique called "select" which allows to wait for multiple events.
Different OS have different implementations of "select" (*nix systems have POSIX select(), Windows has IOCP, etc.)
Python has unified API for all of them in selectors module.

We handle multiple connections in a single thread using "select" system call.
"""


def handle_client_selectors(client_socket, mask, clients, selector):
    if mask & selectors.EVENT_READ:
        if client_socket in clients:
            try:
                data = client_socket.recv(1024)
                if not data:
                    print(f'Connection closed by {client_socket.getpeername()}')
                    selector.unregister(client_socket)
                    client_socket.close()
                    del clients[client_socket]
                else:
                    try:
                        number = int(data.decode())
                        result = str(number ** 2).encode()
                        clients[client_socket]['write_data'] = result
                        clients[client_socket]['write_action'] = 'write'  # Set write action
                        selector.modify(client_socket, selectors.EVENT_WRITE)  # Register for write events
                    except ValueError:
                        result = b'Wrong input'
                        clients[client_socket]['write_data'] = result
                        clients[client_socket]['write_action'] = 'write'  # Set write action
                        selector.modify(client_socket, selectors.EVENT_WRITE)  # Register for write events
            except BlockingIOError:
                pass  # No data to read, handle this case gracefully

    elif mask & selectors.EVENT_WRITE:
        if client_socket in clients:
            action = clients[client_socket].get('write_action')
            data = clients[client_socket].get('write_data')
            if action == 'write':
                try:
                    sent = client_socket.send(data)
                    if sent == len(data):
                        clients[client_socket]['write_action'] = None
                        selector.modify(client_socket, selectors.EVENT_READ)  # Switch back to read mode
                except BlockingIOError:
                    pass  # Socket not ready for writing yet


def square_server_selectors(host, port):
    """
    Use 'selectors' module to handle multiple connections
    DefaultSelector() is API for "select" system call on POSIX systems
    We can subscribe to different events on different sockets
    In this case we subscribe to EVENT_READ on server socket and EVENT_READ on client sockets
    In the pair
    `key, events in selector.select()`
    * `key` is a SelectorKey object with fileobj attribute which is a socket object
    * `events` is a mask of events which are ready to be handled
    * `key.events` is a mask of events we subscribed to, it's equal to `events`
    * `key.data` is a custom data we passed to register() method

    `client_socket.setblocking(False)` makes the socket non-blocking
    we also register it in the selector for EVENT_READ events
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server is listening on {host}:{port}')

        selector = selectors.DefaultSelector()
        selector.register(server_socket, selectors.EVENT_READ)

        clients = {}

        def signal_handler(_1, _2):
            print("Shutting down the server...")
            selector.unregister(server_socket)
            server_socket.close()
            for client_socket in clients:
                selector.unregister(client_socket)
                client_socket.close()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        while True:
            for key, events in selector.select():
                if key.fileobj == server_socket:
                    client_socket, client_address = server_socket.accept()
                    print(f'Connected by {client_address}')
                    client_socket.setblocking(False)
                    selector.register(client_socket, selectors.EVENT_READ)
                    clients[client_socket] = {'write_action': None, 'write_data': None}
                else:
                    handle_client_selectors(key.fileobj, events, clients, selector)


if __name__ == '__main__':
    """
    Choose one of servers accepting connections host:port and run it
    """
    function = sys.argv[1]
    try:
        globals()[function]('127.0.0.1', 10001)
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")

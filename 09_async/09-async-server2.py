import asyncio
import signal


async def handle_client(reader, writer):
    client_address = writer.get_extra_info('peername')
    print(f'Connected by {client_address}')

    while True:
        data = await reader.read(1024)
        if not data:
            break
        try:
            number = int(data.decode())
            print(f'Received {number} from {client_address}')
            result = str(number ** 2).encode()
        except ValueError:
            result = b'Wrong input'
        except Exception as e:
            result = str(e).encode()

        print(f'Sending {result} to {client_address}')
        writer.write(result)
        await writer.drain()

    print(f'Connection closed by {client_address}')
    writer.close()


def signal_handler(_1, _2):
    print("Shutting down the server...")
    loop.stop()


async def square_server_async(host, port):
    server = await asyncio.start_server(handle_client, host, port)
    await server.serve_forever()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    loop = asyncio.get_event_loop()
    loop.create_task(square_server_async('127.0.0.1', 10001))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

import asyncio
from cursor.controller import CursorBase


class AsyncServerProtocol:
    def __init__(self):
        self.cursor = CursorBase()
        pass

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        self.cursor.move_to(*tuple(message))
        # print('Send %r to %s' % (message, addr))
        # self.transport.sendto(data, addr)


async def server():
    print("Starting UDP server")

    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    # One protocol instance will be created to serve all
    # client requests.
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: AsyncServerProtocol(),
        # local_addr=('127.0.0.1', 9999))
        local_addr=(('0.0.0.0', 9999))
    )

    try:
        await asyncio.sleep(3600)  # Serve for 1 hour.
    finally:
        transport.close()



if __name__ == "__main__":
    asyncio.run(server())


import asyncio

class AsynClientProtocol:
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received:", data.decode())
        pass

        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Connection closed")
        self.on_con_lost.set_result(True)



async def send_message_to(message, ip):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()

    transport, _ = await loop.create_datagram_endpoint(
        lambda: AsynClientProtocol(message, on_con_lost),
        # remote_addr=('10.42.0.1', 9999))
        remote_addr=(ip, 9999))

    try:
        await on_con_lost
    finally:
        transport.close()


if __name__ == '__main__':
    message = "Hello World!"
    ip = '10.42.0.1'
    asyncio.run(send(message, ip))

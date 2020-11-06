import asyncio

from cursor.controller import Cursor
from cursor.monitor import CursorMonitorBase
from network.async_udp_client import send_message_to
from network.async_udp_server import AsynClientProtocol


# Send Message
message = '(100,200)'
ip = '10.42.0.1'
send_message_to(message, ip)


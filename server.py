import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/udp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))

sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    if data:
        fake = Faker()
        fakeMsg = fake.text().encode()
        sent = sock.sendto(fakeMsg, address)
        print('sent back the message {}'.format(fakeMsg))

    print('closing socket')
    sock.close()

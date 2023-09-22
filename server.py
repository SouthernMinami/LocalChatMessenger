import socket
import os
from faker import Faker

# create a UDP socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/udp_socket_file'

# if there is alredy a server address file, delete it
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))

# bind the socket to the client address
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    # receive message
    data, address = sock.recvfrom(4096)

    if data:
        fake = Faker()
        fakeMsg =  fake.text().encode() if data == b'msg' else b'Invalid message'
        # send response random fake message
        sent = sock.sendto(fakeMsg, address)
        print('sent back the message {}'.format(fakeMsg))

    # close the socket
    print('closing socket')
    sock.close()

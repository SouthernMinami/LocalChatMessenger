import socket
import os

# create a UDP socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/udp_socket_file'
address = '/udp_client_socket_file'

message = input('Type "msg" to get a random message: ').encode()

# if there is alredy a client address file, delete it
try:
    os.unlink(address)
except FileNotFoundError:
    pass

# bind the socket to the server address
sock.bind(address)

try:
    # send input message
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    print('waiting to receive')
    # receive response
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()


import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/udp_socket_file'
address = '/udp_client_socket_file'

message = input('Enter message: ').encode()

try:
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()


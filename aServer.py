import socket


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data


def server(port=3000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('172.19.137.183', port))
    sock.listen(1)
    print("Start listening...")
    while True:
        print('Waiting for a new connection')
        sc, sockname = sock.accept()
        print('Connection from', sockname)
        message = recvall(sc, 8)
        print(repr(message))
        if repr(message) == repr(b'Saturday') or repr(message) == repr(b'saturday') \
         or repr(message) == repr(b'SATURDAY'):
            sc.sendall(b'You got it!!')
        else:
            sc.sendall(b'Wrong answer.')
        sc.close()
        print('  Closing socket')


if __name__ == '__main__':
    server()

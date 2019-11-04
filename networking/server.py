import socket, pickle
import getty

# these two can be changed
IP = socket.gethostname()
PORT = 1239


# AF_INET -> IPV4
# SOCK_STREAM -> TCP/IP
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# bind to an IP and port
s.bind((IP, PORT))

# listen, will have a queue of N clients
N = 5
s.listen(N)

# start the server
print('start server')
while True:
    print('waiting for clients ...')
    # client_socket - is an object just like s
    # client_address - a tuple
    client_socket, client_address = s.accept()
    print(f'conected to {client_address}')
    
    # reviceved data
    data_recv = pickle.loads(client_socket.recv(2048))
    print(data_recv)
    
    # send response
    client_socket.send(pickle.dumps({
        'message': 'you did well'
    }))
    # client_socket.send(bytes('u connected', 'utf-8'))
        
        
    client_socket.close()
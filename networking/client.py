import socket, pickle
import getty

# these two can be changed
IP = socket.gethostname()
PORT = 1239


# AF_INET -> IPV4
# SOCK_STREAM -> TCP/IP
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# connect to a host
s.connect((IP, PORT))

# send some data
data = {
    'list': [1,2,3,4,5],
    'a': 12,
    'pic': 'asdasdas'
}
s.send(pickle.dumps(data))

# # response -> what we recieve
# # n -> size of data we recieve in BYTES
# n = 1024
# response = s.recv(8)

# # decode the response
# data = response.decode('utf-8')

# print(data)


resp = pickle.loads(s.recv(2048))
print(resp)


s.close()
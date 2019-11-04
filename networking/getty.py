import json, socket

class getty:
    
    @staticmethod
    def encode_dict(__dict):
        if not isinstance(__dict, dict):
            raise ValueError('the argument must be a dict instance')
        return json.dumps(__dict).encode('utf-8')
    
    @staticmethod
    def decode_dict(__socket):
        if not isinstance(__socket, socket.socket):
            raise ValueError('__socket is not a socket instance')
        data_string = __socket.recv(2048).decode('utf-8')
        return json.loads(data_string)
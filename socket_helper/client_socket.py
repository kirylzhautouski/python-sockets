import socket


class ClientSocket:
    
    def __init__(self, s):
        self.s = s
        
    def __del__(self):
        self.close()
    
    @classmethod
    def connect_to_server(cls, server_host, server_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_host, server_port))

        return cls(s)

    def close(self):
        self.s.close()

    

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))

    #     while True:
    #         s.sendall(input().encode())

    #         data = s.recv(1024)

    #         print("Received", data) 

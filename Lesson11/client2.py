#клієнт 2
import socket

HOST = 'localhost'
PORT = 8000

def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        return data.decode('utf-8')

if __name__ == '__main__':
    message = 'Слава Україні, Героям Слава!'
    response = send_message(message)
    print(f'Response: {response}')

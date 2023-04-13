#сервер через сокет
import socket

HOST = 'localhost'
PORT = 8000

def count_words(sentence):
    words = sentence.split()
    return len(words)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Сервер працює за такими параметрами: {HOST}:{PORT}')

        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f'Received data: {data}')
                word_count = count_words(data)
                response = f'Слів в речені: {word_count}'
                conn.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    start_server()

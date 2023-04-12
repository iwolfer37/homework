
# Створення сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5555))
server_socket.listen(1)

# Очікування підключення клієнта та приймання повідомлень від нього
while True:
    client_socket, client_address = server_socket.accept()
    print('Connected by', client_address)
    while True:
        data = client_socket.recv(1024)
        if not data: break
        print(data.decode('utf-8'))

# Закриття з'єднання з клієнтом та сервером
client_socket.close()
server_socket.close()

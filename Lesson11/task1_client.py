

# Створення клієнта та підключення до сервера
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5555))

# Відправлення повідомлень від клієнта до сервера та приймання повідомлень від сервера
while True:
    message = input()
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print(data.decode('utf-8'))

# Закриття з'єднання з клієнтом та сервером
client_socket.close()

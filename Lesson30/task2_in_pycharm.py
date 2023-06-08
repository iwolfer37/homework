import hashlib
import logging

logging.basicConfig(level=logging.INFO)

class UserAuthentication:
    def __init__(self):
        self.users = {}
        self.favorite_number = 37

    def register(self):
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")

        if username in self.users:
            print("Користувач з таким логіном вже існує.")
            logging.warning(f"Спроба реєстрації з існуючим логіном: {username}")
            return

        hashed_password = self._double_hash_password(password)

        self.users[username] = hashed_password
        print("Реєстрація успішна.")
        logging.info(f"Новий користувач зареєстрований: {username}")

    def login(self):
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")

        if username not in self.users:
            print("Користувача з таким логіном не знайдено.")
            logging.warning(f"Спроба входу з недійсним логіном: {username}")
            return

        hashed_password = self._double_hash_password(password)

        if self.users[username] == hashed_password:
            print("Авторизація успішна.")
            logging.info(f"Користувач {username} успішно ввійшов")
        else:
            print("Неправильний пароль.")
            logging.warning(f"Невірний пароль для користувача {username}")

    def _double_hash_password(self, password):
        hashed_password = self._hash_password(password + str(self.favorite_number))

        for _ in range(int(len(self.users) * 0.3 * len(self.users))):
            hashed_password = self._hash_password(hashed_password + str(self.favorite_number))

        return hashed_password

    def _hash_password(self, password):
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        hashed_password = sha256.hexdigest()
        hashed_password = ''.join(chr(ord(c) ^ self.favorite_number) for c in hashed_password)
        return hashed_password


# Використання класу UserAuthentication
auth = UserAuthentication()

while True:
    print("\nМеню:")
    print("1. Реєстрація")
    print("2. Авторизація")
    print("3. Вихід")

    choice = input("Виберіть опцію: ")

    if choice == "1":
        auth.register()
    elif choice == "2":
        auth.login()
    elif choice == "3":
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")

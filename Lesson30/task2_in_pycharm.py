import hashlib

class UserAuthentication:
    def __init__(self):
        self.users = {}

    def register(self):
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")

        # Перевірка на колізії
        if username in self.users:
            print("Користувач з таким логіном вже існує.")
            return

        # Шифрування пароля
        hashed_password = self._double_hash_password(password)

        self.users[username] = hashed_password
        print("Реєстрація успішна.")

    def login(self):
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")

        # Перевірка наявності користувача
        if username not in self.users:
            print("Користувача з таким логіном не знайдено.")
            return

        hashed_password = self._double_hash_password(password)

        # Перевірка пароля
        if self.users[username] == hashed_password:
            print("Авторизація успішна.")
        else:
            print("Неправильний пароль.")

    def _double_hash_password(self, password):
        # Використовуємо подвійне хешування SHA-256
        sha256 = hashlib.sha256()
        sha256.update(password.encode('utf-8'))
        hashed_password = sha256.digest()

        sha256.update(hashed_password)
        double_hashed_password = sha256.hexdigest()
        return double_hashed_password


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
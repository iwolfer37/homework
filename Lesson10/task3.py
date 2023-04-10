class Invalid_input(Exception):
    def __init__(self, message="Некоректні дані."):
        self.message = message
        super().__init__(self.message)  # Виклик конструктора базового класу (Exception) з аргументом message

def divide_numbers(a, b):
    if b == 0:
        raise Invalid_input("Ділення на нуль.")  # Виклик екземпляру класу Invalid_input з повідомленням "Ділення на нуль."
    else:
        return a / b

try:
    result = divide_numbers(10, 0)  # Спробувати обчислити результат ділення 10 на 0
except Invalid_input as e:
    print(e.message)  # Вивести повідомлення про помилку на екран

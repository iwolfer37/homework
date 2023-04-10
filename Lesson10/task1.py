def get_mon():
    months = {1: "Січень", 2: "Лютий", 3: "Березень", 4: "Квітень", 5: "Травень", 6: "Червень", 7: "Липень", 8: "Серпень", 9: "Вересень", 10: "Жовтень", 11: "Листопад", 12: "Грудень"}

    while True:
        try:
            month_number = int(input("Введіть номер місяця (ціле число від 1 до 12): "))
            if month_number < 1 or month_number > 12:
                print("Номер місяця повинен бути в діапазоні від 1 до 12")
            else:
                return months[month_number]
        except ValueError:
            print("Номер місяця повинен бути цілим числом")

month_name = get_mon()
print("Назва місяця:", month_name)

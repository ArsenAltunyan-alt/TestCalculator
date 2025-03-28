def calculate(q1, q2, v):
    if v == 1:
        return "сложения", q1 + q2
    elif v == 2:
        return "вычитания", q1 - q2
    elif v == 3:
        if q2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return "деления", q1 / q2
    elif v == 4:
        return "умножения", q1 * q2
    else:
        raise ValueError("Неверная операция")

if __name__ == "__main__":
    print("Приветствуем вас в калькуляторе Python")
    q1 = int(input("Введите число 1: "))
    q2 = int(input("Введите число 2: "))
    v = int(input("Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n"))

    operation, result = calculate(q1, q2, v)
    print(f"Результат {operation} = {result}")
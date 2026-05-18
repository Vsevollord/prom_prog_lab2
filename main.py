def add(a, b):
    """
            Прибавление числа a к числу b

            Args:
                a: Первое число
                b: Второе число

            Returns:
                Результат сложения
            """
    return a + b

def subtract(a, b):
    """
            Вычитание числа b из числа a

            Args:
                a: Первое число
                b: Второе число

            Returns:
                Результат вычитания
            """
    return a - b

def multiply(a, b):
    """Умножение (оптимизированная версия)"""
    # Разработчик А: добавил проверку на ноль
    if a == 0 or b == 0:
        return 0
    return a * b

def divide(a, b):
    """
            Деление числа a на число b

            Args:
                a: Первое число
                b: Второе число

            Returns:
                Результат деления
            """

    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def sqrt(a):
    """
        Взятие квадратного корня из числа a

        Args:
                a: Основание

            Returns:
                Результат взятия квадратного корня
        """
    return a**0.5

def square(a):
    """
    Возведение числа a в квадрат

    Args:
            a: Основание

        Returns:
            Результат возведения в квадрат
    """

    return a**2

def power(a, b):
    """
        Возведение числа a в степень b

        Args:
            a: Основание
            b: Степень (целое число)

        Returns:
            Результат возведения в степень
        """
    if b == 0:
        return 1

    if abs(b) > 1000:
        raise ValueError("Exponent too large (max 1000)")

    if b < 0:
        return 1 / (a ** abs(b))
    return a ** b

def floor_divide(a, b):
    """Целочисленное деление (версия разработчика Б)"""
    if b == 0:
        raise ValueError("Cannot floor divide by zero")  # Выбрасывает исключение
    return a // b

def main():
    print("Simple Calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"sqrt(25) = {sqrt(25)}")
    print(f"4 ** 3 = {power(4, 3)}")


if __name__ == "__main__":
    main()
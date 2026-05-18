def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def sqrt(a):
    return a**0.5

def square(a):
    return a**2

def power(a, b):
    if b < 0:
        return 1 / (a ** abs(b))
    return a ** b

def main():
    print("Simple Calculator")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"sqrt(25) = {sqrt(25)}")
    print(f"4**2 = {square(4)}")
    print(f"4 ** 3 = {power(4, 3)}")

if __name__ == "__main__":
    main()
def decoration_operation(func):
    def wrapper(*args):
        first, second = args
        if first < 0 or second < 0:
            return func(first, second, "*")
        elif first == second:
            return func(first, second, "+")
        elif first > second:
            return func(first, second, "-")
        elif first < second:
            return func(first, second, "/")

    return wrapper


@decoration_operation
def calc(first, second, operation):
    match operation:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            return first / second


num1, num2 = map(int, input("вводим пару чисел через пробел: ").split())
print(calc(num1, num2))

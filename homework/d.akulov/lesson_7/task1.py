import random

number_guess = random.randint(1, 10)

while True:
    num = int(input("введи цифру и испытай удачу "))
    if num == number_guess:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")

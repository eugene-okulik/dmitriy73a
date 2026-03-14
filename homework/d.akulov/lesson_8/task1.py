import random

salary = int(input())
bonus = bool(random.randint(0, 1))

print(f"{salary}, {bonus} - ${salary + random.randrange(0, 1000, 100)}" if bonus
      else f"{salary}, {bonus} - ${salary}")

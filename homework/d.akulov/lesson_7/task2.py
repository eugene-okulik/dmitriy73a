words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

# 1й вариант
for key, value in words.items():
    print(key * value)


# 2й вариант
def strange_function():
    strin = ""
    for key, value in words.items():
        strin += key * value + "\n"
    return strin[:-1]


print(strange_function())

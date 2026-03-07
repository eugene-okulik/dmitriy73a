my_dict = {"tuple": (4, True, 2.3, "hello", ["q", "w", "e"]),
           "list": [False, "qwerty", 4, 666.6, "pp"],
           "dict": {1: 10, 2: 20, 3: 30, 4: 40, 5: 50},
           "set": {"q", 1, 2.5, "qw", "111"}}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print(my_dict.get("tuple")[-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_dict["list"].append("something")
my_dict.get("list").pop(1)
print(my_dict["list"])

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict["dict"].update({('i am a tuple',): "and I'm a tomato"})
my_dict.get("dict").pop(1)
print(my_dict["dict"])

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
my_dict["set"].add("new element")
my_dict.get("set").pop()
print(my_dict.get("set"))

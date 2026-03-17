PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST = PRICE_LIST.split()

# про инт упустил-подправил, а дважды печатаем это типо 2 разных кривых варианта))
print({PRICE_LIST[e]: int(PRICE_LIST[e + 1][:-1]) for e in range(0, len(PRICE_LIST) - 1, 2)})

print(dict(zip(PRICE_LIST[::2], [int(e[:-1]) for e in PRICE_LIST[1::2]])))

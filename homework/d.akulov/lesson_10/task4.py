PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST = PRICE_LIST.split()

print({PRICE_LIST[e]: PRICE_LIST[e + 1] for e in range(0, len(PRICE_LIST) - 1, 2)})

print(dict(zip(PRICE_LIST[::2], PRICE_LIST[1::2])))

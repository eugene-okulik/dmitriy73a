result_operation_text = input()
print(int(result_operation_text.split()[-1]) + 10 if result_operation_text.split()[
    -1].isdigit() else "а вдруг придет что то иное:)")

# тут перечитал задание изобразил с индексом но первый вариант мне больше нравится
print(int(result_operation_text[result_operation_text.index(
    ":") + 2:]) + 10 if ":" in result_operation_text
      else "ожидаем строку вида 'результат операции: 42 или результат работы программы: 9'")

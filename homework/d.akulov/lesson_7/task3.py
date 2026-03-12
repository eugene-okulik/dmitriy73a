def working_with_text(text):
    return int(text.split()[-1]) + 10 if text.split()[-1].isdigit() else "а вдруг придет что то иное:)"


print(working_with_text(input()))

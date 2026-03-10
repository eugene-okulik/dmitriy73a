import string

# текст для изобретения велосипеда
# text = ("Etiam tincidunt neque erat , quis molestie enim imperdiet vel !!! "
#         "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero!!!")

# исходный текст
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, "
        "facilisis vitae semper at, dignissim vitae libero")

text_final = ""
for word in text.split():
    if word.isalpha():
        text_final += word + "ing "
        continue
    # тут было скучно, решил чуток пострадать над обработкой случаев))
    elif word in string.punctuation or all(e in string.punctuation for e in word):
        text_final += word + " "
    else:
        index_punctuation = None
        for i in range(len(word)):
            if word[i] in string.punctuation:
                index_punctuation = i
                break
        text_final += word[:index_punctuation] + "ing" + word[index_punctuation:] + " "
print(text_final.strip())

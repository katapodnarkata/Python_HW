phrase = input("Введите фразу: ")
change_phrase = phrase.replace(" ", "").lower()

if change_phrase == change_phrase[-1::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")

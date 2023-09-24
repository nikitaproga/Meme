meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "шутка",
            "КРИПОВЫЙ": "страшный, пугающий",
            "ЩИЩ": "одобрение или восторг"
            }
            
name = input("Введите своё имя: ")
print("Добро пожаловать,", name)            
while True:
    command = input("Введите команду(добавить, удалить, определить, закончить): ")
    if command == "определить": 
        word = input("Введите непонятное слово (большими буквами!): ")
        
        if word in meme_dict.keys():
            # Что делать, если слово нашлось?
            print(meme_dict[word])
        else:
            # Что делать, если слово не нашлось?
            print("Такого слова нет")
    elif command == "добавить":
        add_key = input("Введите слово")
        add_value = input("Введите его значение")
        meme_dict = [add_key] = add_value
    elif command == "удалить":
        delete_key = input("Какое слово хотите удалить?")
        del meme_dict [delete_key]
    elif command == "закончить":
        break 
    else:
        print("Такой команды нет")

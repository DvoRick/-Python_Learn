score = [] #создаем пустой список
choice = None #оставляем пустое значение

while choice != "0":
    print("""
    
    Рекорды:
    1 - показать рекорты
    2 - добавить реккорд
    3 - удалить последний рек
    4 - удалить на выбор
    5 - сортировать списк рек
    0 - выйти
    """)
    choice = input("выберете команду: ")

    if choice == "0":
        print("до новых всреч! ")
    elif choice == "1":
        print("Ваши рекорды: ")
        if len(score) == 0:
            print("у Вас нет записей(((")
        else:
            for rec in score:
                print(rec)
    elif choice == "2":
        record = input("Введите рекорд: ")
        score.append(record)
    elif choice == "3":
        score.pop()
        print("удалили последний рек: ", score[-1])
    elif choice == "4":
        delrec = input("какой удалить рек?: ")
        if delrec in score:
            score.remove(delrec)
    elif choice == "5":
        score.sort(reverse=True)  #сортировка по убыванию (можно без нее)
        for rec in score:
            print(rec)

# страница 136 учебника
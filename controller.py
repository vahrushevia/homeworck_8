import echo


def run():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть класс  и место которое занимает  студент \n \
    3: Выход\n \
    Ваш выбор: '))
    
    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in echo.stud_card['Фамилия']:
            index = echo.stud_card['Фамилия'].index(Surn)
        print(f"{echo.stud_card['ID'][index]}, {echo.stud_card['Имя'][index]},{echo.stud_card['Фамилия'][index]}\n,{echo.stud_card['Дата рождения'][index]}, {echo.stud_card['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            run()
        exit()

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in echo.class_card['ID']:
            index = echo.class_card['ID'].index(c)
            print(f" Сидит в классе - {echo.class_card['Предмет'][index]}\n\, за партой номер - {echo.class_card['Номер парты'][index]}, это {echo.class_card['Ряд'][index]}, парта - {echo.class_card['Вид парты'][index]}, Имя: {echo.stud_card['Имя'][index]}, Фамилия - {echo.stud_card['Фамилия'][index]}, и успеваемасть у студента: {echo.stud_card['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                run()
            exit()
    else:
        print('Спасибо')
    exit()
   

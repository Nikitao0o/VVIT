from text_generator import gen
gen() #Генератор случайного текста lorem ipsum

#Задание 1 | 3
def task1(name_file):
    '''
    Выводит на экран содержимое текстового документа
    '''
    try:
        with open(name_file + ".txt", 'r') as f:
            type_read = int(input("""Выберите тип чтения
            1 - чтение файла в 1 строку
            2 - чтение каждого параграфа в элемент списка
            3 - чтение каждого слова в элемент списка
            """))
            types = [1,2,3]
            while type_read not in types:
                print("Нет выбранного типа чтения")
                type_read = int(input("""Выберите тип чтения
                1 - чтение файла в 1 строку
                2 - чтение каждого параграфа в элемент списка
                3 - чтение каждого слова в элемент списка
                """))
            if type_read == 1:
                return f.read()
            elif type_read == 2:
                return f.readlines()
            elif type_read == 3:
                return f.read().split()

    except FileNotFoundError:
        print("Выбранного текстового файла не существует.")
    except ValueError:
        print("Недопустимый ввод.")
#Задание 2
def task2():
    '''Сохраняет введенный текст в файл user_input.txt'''
    with open("user_input.txt", "a+") as f: #Флаг а+ позволяет добавлять ввод в конец файла, если файла не существует, он будет создан
        f.write(input('Введенный текст будет добавлен в файл ввода:'))

#Задание 2 (с помощью stdin)
import sys
def std_task2():
    '''
        Сохраняет введенный текст в файл user_input.txt
        и позволяет вводить неограниченное количество строк
    '''
    f = True
    while f:
        try:
            with open("user_input.txt", "a+") as f:
                print('Введенный текст будет добавлен в файл ввода:\n(ctrl-d Для завершения ввода)')
                for s in sys.stdin.readlines():
                    f.write(s)
                print("Ввод завершен.")
                f = False
        except KeyboardInterrupt:
            f = False


if input("Что пожелаете?\n 1 - Задание 1 | 3\n 2 - Задание 2\n") == '1':
    print(task1(input("Введите имя текстового файла к прочтению\n")))
else: std_task2()

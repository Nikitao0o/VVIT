def task1():
    for i in range(1, int(input("Введите число: "))+1):
        print(i)

def task2():
    print("Большее число:", max(int(input("Введите первое число: ")), int(input("Введите второе число: "))))

def task2v2():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a > b:
        print("Большее число:", a)
    elif b > a:
        print("Большее число:", b)
    else:
        print("Введенные числа равны\n", a, "=", b, sep="")
if __name__ == '__main__':
    task1()
    task2()
    task2v2()

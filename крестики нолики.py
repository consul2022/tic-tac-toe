import random

field = []  # поле

# [[██, ██, ██], [██,██,██], [██,██,██]]

def create_field():  # создание поле списка
    global field     # изменение переменной, локальная на глобальную
    for i in range(3):   #цикл
        field.append(["██"] * 3) #добавляет элемент в конец списка


def print_field(field):
    for i in field: # читерский метод -> [██,██,██]
        print(*i) # * - everything
    print()


def cor_user(a,b): # a = input()
    global field
    a = int(a[-1])
    b = int(b[-1])
    while field [a-1][b-1] !="██":
        print("Эта ячейка занята, сделайте ход в другую ячейку")
        a,b = int(input()[-1]),int(input()[-1])
    # input() = "A3" -> 3
    # int(a[-1])
    # [2][2] -> A3 B3
    field[a - 1][b - 1] = user


def cor_computer():
    global field
    a = random.randint(1,3)
    b = random.randint(1,3)
    while field[a - 1][b - 1] != "██":
        a = random.randint(1,3)
        b = random.randint(1,3)
    field[a - 1][b - 1] = computer
# x x x
# x x x
# x x x
def check():
    if field[0][0] == field[0][1] == field[0][2] !="██" \
        or field [1][0] == field [1][1] == field [1][2] !="██" \
        or field [2][0] == field [2][1] == field [2][2] !="██"\
        or field [0][0] == field [1][0] == field [2][0] !="██"\
        or field [0][1] == field [1][1] == field [2][1] !="██"\
        or field [0][2] == field [1][2] == field [2][2] !="██"\
        or field [0][0] == field [1][1] == field [2][2] !="██"\
        or field [0][2] == field [1][1] == field [2][0] !="██":
        return True
    return False

def draw(): #ничья
    for i in field: # i = [██,██,██]
        if i.count("██") != 0:
            return False
    return True

create_field()
print_field(field)
user = "X "
computer = "0 "
while True:
    a = input()
    b = input()
    cor_user(a, b)
    if draw():
        break
    if check():
        print("Вы выйграли !")
        print_field(field)
        break


    cor_computer()
    print_field(field)
    if draw():
        break
    if check():
        print("Вы проиграли !")
        print_field(field)
        break








def sum_two_number(a, b):
    print(f'Сумма {a} + {b} = {a + b}')
    return


def difference(a, b):
    print(f'разность {a} - {b} = {a - b}')


def multiply(a, b):
    print(f'умножить {a} * {b} = {a * b}')


def share(a, b):
    print(f'разделить {a} / {b} = {a / b}')

while True:
    c = input('Введите знак (+,-,*,/): ')
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))

    if c == '+':
        sum_two_number(a, b)
    elif c == '-':
        difference(a, b)
    elif c == '*':
        multiply(a, b)
    elif c == '/':
        if b != 0:
            print(a / b)
        else:
            print('Делить на 0 нельзя')
        share(a, b)
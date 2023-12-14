import random

# hw_task_1.1

# strlen = lambda s: len(s)
# print(strlen("Dlina str"))
def stringlen(s):
    print(f"Задание №1\nДлина строки: {len(str(s))}")

stringlen("skolko tut?")

# hw_task_1.2
def arraycomp(a1,a2):
    if len(a1) > len(a2):
       print(f"\nЗадание №2\nПервый список больше: {len(a1)}")
    else:
       print(f"\nЗадание №2\nВторой список больше: {len(a2)}")


arraycomp([1,2,3,5],[5,7,8,9,54])


# hw_task_1.3

def arrayrandom():
    r_array = [random.randint(1, 100) for _ in range(10)]
    print(f"\nЗадание №3\nСписок с произвольными значениями: {r_array}")
    r_array.append(random.randint(1,100))
    print(f"\nПлюс произвольное изначение: {r_array}")

arrayrandom()


# hw_task_1.4

def chislo(a):
    if a>100 or a<-100:
        print("\nЗаданиие №4\nРезультат: -")
    else:
        print("\nЗаданиие №4\nРезультат: +")

chislo(289)


# hw_task_1.5

str_1 = 'test'
str_2 = 'test1'

def str_compare():
    if str_1 in str_2:
        print("\nЗадание №5\nРезультат: Да")
    else:
        print("\nЗадание N5\nРезультат: Нет")

str_compare()


# hw_task_1.6

def list_positive(list_1):
    positive_num = 0
    for numb in list_1:
        if numb > 0:
            positive_num +=1

    print(f"\nЗадание №6\nПоложительных чисел: {positive_num}")

list_positive([1,2,-10,-4,5])


# hw_task_1.7

def total_days(y,m):
    print(f"\nЗадание№7\nКоличество дней: {(29*m + 12*29*y)}")

total_days(0,4)


# hw_task_1.8

def short_str(str_3):
    #if type(str_3) is str:
    try:
        words = str_3.split()
        f_letters = [word[0] for word in words]
        print("\nЗадание №8\n" + ''.join(f_letters))
    except:
        print("\nЗадание №8\nВведена не строка")

short_str("asdasd tuetrt asdaf fghfgh")


# hw_task_1.9

def factorial(f):
    fact = 1
    for i in range(1,f+1,1):
        fact *= i

    print(f"\nЗадание №9\nФакториал числа {f}: {fact}")

factorial(8)


# hw_task_1.10

# исходный код:
lst = [2,4,5,8,9,13]

for number in range(len(lst)):
    lst[number] *= number

print(f"\nЗадание№10\nРезультат исходного кода:{lst}")


# другая конструкция:
lst_1 = [2,4,5,8,9,13]
i = 0

while i != len(lst_1):
    lst_1[i] *= i
    i+= 1

print(f"Результат измененного кода:{lst_1}")
import random
# 1 -----
print("------")
print("TASK 1")
print("------")


def func1(st):
    stop_list = ['Python', 'php', 'go', 'C']
    return " ".join(list(filter(lambda x: x not in stop_list, st.split())))


test_string = 'Python is better than go or php or C or fortran'
print(func1(test_string))

# 2 -----
print("------")
print("TASK 2")
print("------")


def func2(st):
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list(filter(lambda x: x % st == 0, list_1))


for i in range(1, 10):
    print(func2(i))

# 3 -----
print("------")
print("TASK 3")
print("------")


def func3(*args):
    tuple_ = ()
    for item in args:
        if isinstance(item, str):
            tuple_ += (item,)
    return tuple_


print(func3(1, 2, 3, 4, 5, 'kek', 'foo'))

# 4 -----
print("------")
print("TASK 4")
print("------")

def func4(list_1,list_2):
    return list(filter(lambda x: x in list_2, list_1))


list_1 = [1, 2, 3, 4, 5, 'kek', 'foo']
list_2 = [2,6,'foo',10, 5]

print(func4(list_1,list_2))

# 5 -----
print("------")
print("TASK 5")
print("------")


# Что-то я не очень понял задание

# 6 -----
print("------")
print("TASK 6")
print("------")

def decorated(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        #print(type(args))
        if not isinstance(result, int):
#            print('not an int')
            raise ValueError('!! Это не int!!')
        else:
            print('ok')
        return result
    return wrapper

@decorated
def testfun_1():
    a = random.choice([1,10.0,'some str'])
    print("test func value 1 : ", a)
    return a

#testfun_1()

# 7 -----
print("------")
print("TASK 7")
print("------")
def decorated2(fn):
    def wrapper(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except:
            print('сработал exception, запускаем еще раз')
            fn(*args, **kwargs)
    return wrapper
@decorated2
def testfun_new():
    a = random.choice([1,2])
    if random.choice([True,False]):
        1/0
        #raise ValueError('случайный exception')
    else:
        print('ok, not an exception')
    return a

#testfun_new()


# 8 -----
print("------")
print("TASK 8")
print("------")


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
elements.sort(key=lambda x: x[1])
print(elements)


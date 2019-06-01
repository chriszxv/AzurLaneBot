b = 0


def my_fun():
    global b
    b = b + 10


my_fun()
print(b)

def func():
    print('Function Started')

    x = yield
    print(x)
    print('Function part 2')

    a = yield
    print(a)
    print('Function part 3')


try:
    y = func()
    next(y)
    y.send(6)
    y.send(12)

except StopIteration as e:
    pass

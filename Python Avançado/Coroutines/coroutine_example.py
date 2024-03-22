def func():
    print('Function Started')

    yield

    print('Function Finished')


try:
    y = func()
    print(type(y))
    next(y)
    next(y)
except StopIteration as e:
    pass

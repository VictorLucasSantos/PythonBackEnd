def func():
    x = 5
    print('Function Part 1')

    yield x
    x += 7
    print('Function Part 2')

    yield x

    print('Function Part 3')


try:
    # main function
    y = func()

    # function part 1
    z = func()
    print(z)

    # function part 2
    z = next(y)
    print(z)

    z = next(y)
    print(z)
except StopIteration as e:
    pass

def my_gen():
    n = 1
    print('Primeiro print'.format(n))
    yield n

    n += 1
    print('Segundo print'.format(n))
    yield n

    n += 1
    print('Terceiro e ultimo print'.format(n))
    yield n

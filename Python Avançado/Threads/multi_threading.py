import time
import threading


def calc_square(numbers):
    print('calculate square numbers')
    for number in numbers:
        time.sleep(2)
        print('Square: {} '.format(number * number))


def calc_cube(numbers):
    print('calculate cube of numbers')
    for number in numbers:
        time.sleep(2)
        print('Cube: {} '.format(number * number * number))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]

    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('done')
    
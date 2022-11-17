import os
from debug_utils import logger


def test_1():
    path = 'mainlog.txt'
    if os.path.exists(path):
        os.remove(path)


@logger
def hello_world():
    return 'Hello World'


@logger
def summator():
    a = int(input('Enter your two numbers for sum:\n'))
    b = int(input())
    return f'Your two numbers are --> {a} and {b}\nSum --> {a + b}'


@logger
def div():
    a = int(input('Enter your two numbers for division:\n'))
    b = int(input())
    return f'Your two numbers are --> {a} and {b}\nDivision --> {a / b}'


if __name__ == '__main__':
    test_1()
    hello_world()
    summator()
    div()








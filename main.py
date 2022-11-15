import os
from debug_utils import logger


#def test1():


@logger
def hello_world():
    return 'Hello World'


@logger
def summator(a, b):
    return f'Your two numbers are --> {a} and {b}\nSum --> {a + b}'


@logger
def div(a, b):
    return f'Your two numbers are --> {a} and {b}\nDivision --> {a / b}'


if __name__ == '__main__':
    hello_world()
    summator(2, 3)
    div(6, 3)






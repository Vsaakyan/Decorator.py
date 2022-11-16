from debug_utils import logger


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
    hello_world()
    summator()
    div()








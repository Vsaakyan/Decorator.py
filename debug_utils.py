import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        path = 'mainlog.txt'
        with open(path, 'a', encoding= 'utf-8') as file:
            file.write(f'-- You called function {old_function.__name__} \n-- Arguments are: {args, kwargs} \n-- '
                       f'Date and time of calling this fucntion is : {datetime.datetime.now()} \n-- Result is: {result}')
    return new_function

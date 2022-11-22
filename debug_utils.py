import datetime


def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding= 'utf-8') as file:
                file.write(f'-- YOU CALLED FUNCTION: {old_function.__name__} \n-- Arguments are: {args, kwargs} \n-- '
                           f'Date and time of calling this fucntion is : {datetime.datetime.now()} \n-- Result is: {result}\n')
            return result

        return new_function
    return _logger



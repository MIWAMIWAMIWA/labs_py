"""
this module have decorator functions
"""
import inspect
import logging


def logging_arguments(func):
    """
    this decorator prints to file : name_of_function : name_of_argument = value_of_argument
    """

    def wrapper(*args):
        with open("arguments.txt", 'a', encoding="utf-8") as file:
            for name, value in zip(inspect.getfullargspec(func).args, args):
                if name != 'self':
                    file.write(func.__name__ + " : " + name + " = " + str(value) + "\n")
        return func(*args)

    return wrapper


def logging_exception(func):
    """
    this decorator prints to file : name_of_function raised TypeOfException
    """

    def wrapper(*args):
        try:
            return func(*args)
        except Exception as exception:
            with open("exceptions.txt", 'a', encoding="utf-8") as file:
                file.write(func.__name__ + " raised " + type(exception).__name__ + "\n")
            raise

    return wrapper


def logged(exception, mode):
    """
    decorator that works in 2 modes:
    1.mode = console :
    will print exception that raised in decorated function to console
    2.mode = file:
    will print exception that raised in decorated function to file
    """
    def decorator(func):
        def wrapper(*args):
            try:
                return func(*args)
            except exception as current_exception:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                elif mode == "file":
                    logging.basicConfig(filename='new_exceptions.txt',
                                        filemode='a', level=logging.INFO)
                logging.exception(current_exception)

        return wrapper

    return decorator

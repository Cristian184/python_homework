import logging 
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        pos = args if args else "none" 
        kw = kwargs if kwargs else "none"
        value = func(*args, **kwargs)
        logger.log(logging.INFO,
                   f"function: {func.__name__} | "
                   f"positional parameters: {pos} | "
                   f"keyword parameters: {kw} | "
                   f"return: {value}"
                   )
        return value
    return wrapper

@logger_decorator
def hello():
    print("Hello World!")

@logger_decorator
def true(*args):
    return true

@logger_decorator
def kwarg(**kwargs):
    return logger_decorator

hello()
true(1, 5, 7)
kwarg(x=5, y=24)
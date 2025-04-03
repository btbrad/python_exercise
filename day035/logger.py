from functools import wraps

def add_log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print(args)
            with open('./log.txt', 'a+') as file:
                file.write(text+'\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator
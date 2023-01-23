def typecheck(func):
    def wrapper(*args, **kwargs):
        for arg in kwargs:
            annotation = func.__annotations__[arg]
            input_type = type(kwargs[arg])
            if annotation != input_type:
                raise TypeError("Check function/method input-type")

        result = func(*args, **kwargs)
        return result
    return wrapper
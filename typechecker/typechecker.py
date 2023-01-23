def typecheck(func):
    def wrapper(*args, **kwargs):
        for kwarg in kwargs:
            annotation = func.__annotations__[kwarg]
            input_type = type(kwargs[kwarg])

            if annotation == input_type:
                continue

            elif annotation != input_type:
                raise TypeError("Check function/method input-type(s)")
            
        result = func(*args, **kwargs)
        return result
    return wrapper
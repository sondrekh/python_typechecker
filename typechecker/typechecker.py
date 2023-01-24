def typecheck(func):
    """Decorator used to enforce type-hints."""
    def decorated_function(*args, **kwargs):
        annotations = func.__annotations__

        check_kwargs(kwargs, annotations)
        
        if len(args) != 1:
            handle_args(args, annotations)
       
        result = func(*args, **kwargs)
        return result

    return decorated_function



def check_kwargs(kwargs, annotations):
    """Typecheck for each provided kwarg."""
    for kwarg in kwargs:
        check_type(annotations[kwarg], type(kwargs[kwarg]))


def handle_args(args, annotations):
    """Typecheck each provided argument without keywords."""
    i = 1 # First argument in "args" is "self". First input arg is at index 1.
    for annotation in annotations:
        if annotation == "return": # Return-value-annotation, not input. 
            break

        check_type(type(args[i]), annotations[annotation])
        i += 1 


def check_type(type_input, type_expected): 
    if type_input != type_expected:
        raise TypeError("Check function/method input-type(s)")
def typecheck(func):
    """Decorator used to enforce type-hints."""
    def decorated_function(*args, **kwargs):
        Typecheck(func, *args, **kwargs)       
        result = func(*args, **kwargs)
        return result

    return decorated_function

class Typecheck:
    """Takes input types for args and kwargs and checks against function type hints."""
    def __init__(self, func: callable, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs
        self.annotations = func.__annotations__

        self.check_kwargs()

        if len(args) != 1: # If len == 1, the only argument is "self"
            self.check_args() 

    def check_args(self):
        """Typecheck each provided argument without keywords."""
        i = 1 # First argument in "args" is "self". First input arg is at index 1.
        for annotation in self.annotations:
            if annotation == "return": # Return-value-annotation, not input. 
                break

            check_type(type(self.args[i]), self.annotations[annotation])
            i += 1

    def check_kwargs(self):
        """Typecheck for each provided kwarg."""
        for kwarg in self.kwargs: 
            check_type(self.annotations[kwarg], type(self.kwargs[kwarg]))
    

def check_type(type_input, type_expected): 
    """Compare provided types. Raise TypeError exception if mismatch."""
    if type_input != type_expected:
        raise TypeError("Check function/method input-type(s)")



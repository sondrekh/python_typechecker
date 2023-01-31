class Typecheck:
    """Takes input types for args and kwargs and checks against function type hints."""

    def __init__(self, _type, func: callable, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs
        self.annotations = func.__annotations__

        self.check_kwargs()

        minimum_length = 1
        if _type == "FUNCTION":
            minimum_length = 0

        if len(args) != minimum_length:  # If len == 1, the only argument is "self" for class methods
            self.check_args(minimum_length)

    def check_args(self, i: int) -> None:
        """Typecheck each provided argument without keywords."""
        for annotation in self.annotations:
            if annotation == "return":  # Return-value-annotation, not input.
                break

            check_type(type(self.args[i]), self.annotations[annotation])
            i += 1

    def check_kwargs(self) -> None:
        """Typecheck for each provided kwarg."""
        for kwarg in self.kwargs:
            check_type(self.annotations[kwarg], type(self.kwargs[kwarg]))


def check_type(type_input: type, type_expected: type) -> None:
    """Compare provided types. Raise TypeError exception if mismatch."""
    equalTypes = False

    if type_input == type_expected:  # Check if types matches
        equalTypes = True
    else:  # If types doesn't match, check if a parent class matches.
        equalTypes = check_parent_classes(type_expected, type_input)

    if not equalTypes:
        raise TypeError("Check function/method input-type(s)")


def check_parent_classes(expected: type, input: type) -> bool:
    """Check if input class has a parent class matching the expected type."""
    equalTypes = False
    _type = input

    while _type != object:  # Check if "object", as object is at top level for all types.
        _type = get_parent_class(_type)
        if expected == _type:
            equalTypes = True  # If matching comparing object, no need for further checks
            break

    return equalTypes


def get_parent_class(object) -> type:
    """type.__bases__ returns "(<class 'str',)"."""
    bases = object.__bases__
    return bases[0]

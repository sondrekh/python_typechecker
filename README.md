# Typechecker

Functionality:

-   Compare typehints against args
-   Compare typehints against key-word args
-   Check parent classes for non-matching type

Works for both functions and class methods.

```python
class Foo:
    @typecheck
    def bar(self, baz: str) -> None:
        print(baz)

foo = Foo()
foo.bar("baz")
# baz
foo.bar(1)
# TypeError: Check function/method input-type(s)
```

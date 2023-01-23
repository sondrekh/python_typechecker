import unittest
from typechecker import typecheck

class Foo:
    @typecheck
    def bar(self, someString: str) -> None:
        self._bar = someString

class Typecheck_for_single_arg(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = Foo()

    def test_fail_instantiation_of_typecheck_decorated_method_arg(self):
        self.assertRaises(TypeError, self.foo.bar, 1)


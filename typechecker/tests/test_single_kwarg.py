import unittest
from typechecker import typecheck

class Foo:
    @typecheck
    def bar(self, someString: str) -> None:
        self._bar = someString

class Typecheck_for_single_kwarg(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = Foo()

    def test_fail_instantiation_of_typecheck_decorated_method(self):
        self.assertRaises(TypeError, self.foo.bar, someString=5)

    def test_should_work_if_input_is_matching_annotations(self):
        value = "hello world"
        self.foo.bar(someString=value)
        self.assertEqual(value, self.foo._bar)

    def test_fail_if_error_in_kw_spelling(self):
        self.assertRaises(KeyError, self.foo.bar, not_a_kw="Fail!")
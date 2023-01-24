import unittest
from typechecker import typecheck

class Bar:
    pass

class NotBar:
    pass

class Foo:
    @typecheck
    def bar(self, someString: str, someInt: int, someBar: Bar) -> None:
        self.someString = someString
        self.someInt = someInt
        self.someBar = someBar

class Typecheck_for_multiple_args(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = Foo()


    def test_success_if_all_arg_types_are_matching(self):
        someString = "Success"
        someInt = 1
        someBar = Bar()

        self.foo.bar(someString, someInt, someBar)

        self.assertEqual(self.foo.someString, someString)
        self.assertEqual(self.foo.someInt, someInt)
        self.assertEqual(self.foo.someBar, someBar) 

    def test_fail_if_single_mismatch(self):
        someString = "Success"
        someInt = 1
        someBar = NotBar()

        self.assertRaises(TypeError, self.foo.bar, someString, someInt, someBar)
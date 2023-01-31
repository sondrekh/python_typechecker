import unittest
from typechecker import typecheck


@typecheck
def foo(bar: str):
    return bar.upper()


class TestTypecheckerForFunctions(unittest.TestCase):

    def test_should_raise_error_when_using_int_for_str(self):
        self.assertRaises(TypeError, foo, 1)

    def test_should_pass_if_correct_input(self):
        self.assertEqual("BAR", foo("bar"))

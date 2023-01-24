import unittest

from typechecker import typecheck

class Bar:
    ...

class BarChild(Bar):
    ...

class NotBar:
    ...

class Foo:
    @typecheck
    def bar(self, someBar: Bar):
        self._bar = someBar

class TestSubClassHandling(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = Foo()

    def test_accept_class_of_hinted_class_type(self):
        bar = Bar()

        self.foo.bar(bar)

        self.assertEqual(bar, self.foo._bar)

    def test_fail_class_of_hinted_class_type_mismatch(self):
        self.assertRaises(TypeError, self.foo.bar, NotBar())

    
    def test_accept_subclass_of_bar(self):
        bar = BarChild()

        self.foo.bar(bar)

        self.assertEqual(bar, self.foo._bar)
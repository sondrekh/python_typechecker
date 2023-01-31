import unittest

from typechecker import typecheck


class Bar:
    ...


class BarChild(Bar):
    ...


class SubBarChild(BarChild):
    ...


class SubSubBarChild(SubBarChild):
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


class SubClassExploratory(unittest.TestCase):

    def test_find_parent_class_for_child(self):
        parent = Bar()
        child = BarChild()

        isChild = is_child_and_parent_classes(parent, child)

        self.assertTrue(isChild)

    def test_find_grandparent_class(self):
        grandparent = Bar()
        subchild = SubBarChild()

        isChild = is_child_and_parent_classes(grandparent, subchild)

        self.assertTrue(isChild)

    def test_find_greatgrandparent_class(self):
        grandparent = Bar()
        subchild = SubSubBarChild()

        isChild = is_child_and_parent_classes(grandparent, subchild)

        self.assertTrue(isChild)


def is_child_and_parent_classes(class_object, other):
    areEqual = False
    _type = type(other)

    while _type != object:  # Check if "object", as object is at top level for all types.
        _type = get_parent_class(_type)
        if type(class_object) == _type:
            areEqual = True  # If matching comparing object, no need for further checks
            break

    return areEqual


def get_parent_class(object) -> type:
    """type.__bases__ returns "(<class 'str',)"."""
    bases = object.__bases__
    return bases[0]

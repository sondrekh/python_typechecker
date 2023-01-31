import unittest
from typechecker import typecheck


class Bar:
    def __init__(self) -> None:
        self.foo = 5


class Alpha:

    def __init__(self) -> None:
        print("Hello world")


class Foo:
    @typecheck
    def bar(self, alpha: str, beta: int, gamma: Bar) -> None:
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma


class Typecheck_for_multiple_kwargs(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = Foo()

    def test_match_on_all_annotations(self):
        alpha = "alpha"
        beta = 1
        gamma = Bar()

        self.foo.bar(alpha=alpha, beta=beta, gamma=gamma)

        self.assertEqual(alpha, self.foo.alpha)
        self.assertEqual(beta, self.foo.beta)
        self.assertEqual(gamma, self.foo.gamma)

    def test_mismatch_on_class_kwarg(self):
        alpha = "alpha"
        beta = 1
        gamma = Alpha()

        self.assertRaises(TypeError, self.foo.bar,
                          alpha=alpha, beta=beta, gamma=alpha)

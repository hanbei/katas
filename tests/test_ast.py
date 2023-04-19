import pytest

from katas.ast import *


def test_creation():
    operation = Add(Value(3.0), Value(2.0))
    print(operation)


def test_print_visitor():
    add = Add(Value(3.0), Value(2.0))
    mul = Mul(Value(2.0), add)
    div = Div(mul, Value(2.0))
    sub = Sub(div, Value(3.0))

    print()
    sub.accept(RPNVisitor())
    print()
    sub.accept(InfixVisitor())
    eval = Evaluator()
    sub.accept(eval)

    assert eval.result() == pytest.approx(2.0)


def test_parse():
    ast = parse("3 6 +")
    eval = Evaluator()
    ast.accept(eval)
    assert eval.result() == pytest.approx(9.0)

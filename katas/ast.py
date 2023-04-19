from abc import ABC, abstractmethod
from collections import deque


class Visitor(ABC):
    @abstractmethod
    def visitDiv(self, div):
        pass

    @abstractmethod
    def visitMul(self, mul):
        pass

    @abstractmethod
    def visitSub(self, sub):
        pass

    @abstractmethod
    def visitAdd(self, add):
        pass

    @abstractmethod
    def visitValue(self, value):
        pass


class RPNVisitor(Visitor):

    def visitDiv(self, node):
        node._left.accept(visitor=self)
        node._right.accept(visitor=self)
        print(" / ", end='')

    def visitMul(self, node):
        node._left.accept(visitor=self)
        node._right.accept(visitor=self)
        print(" * ", end='')

    def visitSub(self, node):
        node._left.accept(visitor=self)
        node._right.accept(visitor=self)
        print(" - ", end='')

    def visitAdd(self, node):
        node._left.accept(visitor=self)
        node._right.accept(visitor=self)
        print(" + ", end='')

    def visitValue(self, node):
        print(node._value, end=' ')


class InfixVisitor(Visitor):

    def visitDiv(self, node: 'Div'):
        print("(", end='')
        node._left.accept(visitor=self)
        print(" / ", end='')
        node._right.accept(visitor=self)
        print(")", end='')

    def visitMul(self, node):
        print("(", end='')
        node._left.accept(visitor=self)
        print(" * ", end='')
        node._right.accept(visitor=self)
        print(")", end='')

    def visitSub(self, node):
        print("(", end='')
        node._left.accept(visitor=self)
        print(" - ", end='')
        node._right.accept(visitor=self)
        print(")", end='')

    def visitAdd(self, node):
        print("(", end='')
        node._left.accept(visitor=self)
        print(" + ", end='')
        node._right.accept(visitor=self)
        print(")", end='')

    def visitValue(self, value):
        print(f"{value._value}", end='')


class Evaluator(Visitor):

    def __init__(self):
        self._calculation = 0

    def visitDiv(self, node: 'Div'):
        node._left.accept(self)
        left = self._calculation
        node._right.accept(self)
        right = self._calculation
        self._calculation = left / right

    def visitMul(self, node: 'Mul'):
        node._left.accept(self)
        left = self._calculation
        node._right.accept(self)
        right = self._calculation
        self._calculation = left * right

    def visitSub(self, node: 'Sub'):
        node._left.accept(self)
        left = self._calculation
        node._right.accept(self)
        right = self._calculation
        self._calculation = left - right

    def visitAdd(self, node: 'Add'):
        node._left.accept(self)
        left = self._calculation
        node._right.accept(self)
        right = self._calculation
        self._calculation = left + right

    def visitValue(self, value: 'Value'):
        self._calculation = value._value

    def result(self) -> float:
        return self._calculation


class Ast(ABC):

    def __init__(self, left: 'Ast', right: 'Ast'):
        self._right = right
        self._left = left

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Value(Ast):

    def __init__(self, value: float):
        super().__init__(None, None)
        self._value = value

    def __str__(self) -> str:
        return str(self._value)

    def accept(self, visitor: Visitor) -> None:
        visitor.visitValue(self)


class Add(Ast):
    def __str__(self) -> str:
        return f"{self._left} + {self._right}"

    def accept(self, visitor: Visitor) -> None:
        visitor.visitAdd(self)


class Sub(Ast):
    def __str__(self) -> str:
        return f"{self._left} - {self._right}"

    def accept(self, visitor: Visitor) -> None:
        visitor.visitSub(self)


class Mul(Ast):
    def __str__(self) -> str:
        return f"{self._left} * {self._right}"

    def accept(self, visitor: Visitor) -> None:
        visitor.visitMul(self)


class Div(Ast):
    def __str__(self) -> str:
        return f"{self._left} / {self._right}"

    def accept(self, visitor: Visitor) -> None:
        visitor.visitDiv(self)


def parse(rpn: str):
    stack: deque = deque(rpn.split(' '))

    def rec_parse(x: str):
        if x == '/':
            return Div(rec_parse(stack.pop()), rec_parse(stack.pop()))
        elif x == '*':
            return Mul(rec_parse(stack.pop()), rec_parse(stack.pop()))
        elif x == '+':
            return Add(rec_parse(stack.pop()), rec_parse(stack.pop()))
        elif x == '-':
            return Sub(rec_parse(stack.pop()), rec_parse(stack.pop()))
        else:
            return Value(float(x))

    if len(stack) > 0:
        x = stack.pop()
        return rec_parse(x)

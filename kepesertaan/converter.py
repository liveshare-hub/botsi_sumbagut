from graphene.types import Scalar
from graphql.language import ast
from graphene.types.scalars import MAX_INT, MIN_INT

class BigInt(Scalar):

    @staticmethod
    def big_to_float(value):
        num = int(value)
        if num > MAX_INT or num < MIN_INT:
            return float(int(num))
        return num
    serialize = big_to_float
    parse_value = big_to_float

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.IntValue):
            num = int(node.value)
            if num > MAX_INT or num < MIN_INT:
                return float(int(num))
            return num
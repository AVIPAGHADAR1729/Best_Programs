"""
New Version of Pascal row with prettyfy the rows
"""

from functools import wraps
from math import comb

# ____________________________________________________________________________________ #


def prettyfy(func):
    @wraps(func)
    def wrapper(N):
        return "\n".join([*map(" ".join, func(N))])

    return wrapper


class Pascal:
    @staticmethod
    @prettyfy
    def pascal(N: int) -> list:
        return [
            *map(lambda x: [*map(lambda y: str(comb(x, y)), range(x + 1))], range(N))
        ]
    
    @staticmethod
    @prettyfy
    def pascal_list_comp(N: int):
        return [[str(comb(x, y)) for y in range(x + 1)] for x in range(N)]



if __name__ == "__main__":
    print(Pascal.mro())
    print(Pascal.pascal(10))
    print(Pascal.pascal(20))
    print(Pascal.pascal(50))
    print(Pascal.pascal_list_comp(11))


# ____________________________________________________________________________________ #

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



if __name__ == "__main__":
    print(Pascal.mro())
    print(Pascal.pascal(10))
    print(Pascal.pascal(20))
    print(Pascal.pascal(50))

# ____________________________________________________________________________________ #

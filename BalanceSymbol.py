symbol = {"[": -1, "{": -2, "(": -3, "<": -4, "]": 1, "}": 2, ")": 3, ">": 4}


print(symbol)


def isBalanced(inp):
    stack = []

    for e in inp:

        if symbol[e] < 0:
            stack.append(e)
        else:

            if stack == []:
                return "NO"
            else:
                top = stack.pop()
                if symbol[top] + symbol[e] != 0:
                    return "NO"

    if stack == []:
        return "YES"
    else:
        return "NO"


print(isBalanced("{{}(){}}<>{}{{<<>>}}{}"))

from math import ceil


def solution(X, Y, D):
    # 0 handles special case, otherwise return the ceilling of the expression
    return 0 if X == Y else ceil((Y - X) / D)

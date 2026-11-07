def solution(A):
    # The complete sequence runs from 1 through len(A) + 1.
    n = len(A) + 1
    total = n * (n + 1) // 2

    # Subtract each present value to leave the missing one.
    for value in A:
        total -= value

    return total

def solution(A):
    left_sum = 0
    right_sum = sum(A)
    min_diff = float("inf")

    # Check every cut that leaves both sides nonempty.
    for p in range(1, len(A)):
        # Move one element from the right side to the left side.
        value = A[p - 1]
        left_sum += value
        right_sum -= value

        difference = abs(left_sum - right_sum)
        if difference == 0:
            return 0  # A perfect split cannot be improved.

        min_diff = min(min_diff, difference)

    return min_diff

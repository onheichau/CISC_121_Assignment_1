def solution(A):
    # Return the value that appears an odd number of times
    indices_by_value = {}

    for i in range(len(A)):
        value = A[i]

        # Create an empty index list the first time we see this value.
        if value not in indices_by_value:
            indices_by_value[value] = []

        # Record this occurrence, including the first one.
        indices_by_value[value].append(i)

    for value, indices in indices_by_value.items():
        # Each stored index represents one occurrence of this value.
        if len(indices) % 2 == 1:
            return value

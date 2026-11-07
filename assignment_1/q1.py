# Rotate A to the right by K positions in place and return it
def solution(A, K):
    size = len(A)
    if size == 0:
        return A

    # Every size rotations brings the list back to its starting order
    # K % size also serve as an if statment to early return as needed
    for _ in range(K % size):
        # Save the last element before start writing
        last_element = A[-1]

        # Shift from right to left so each value is read before it is overwritten
        for i in range(size - 1, 0, -1):
            A[i] = A[i - 1]

        # Wrap the saved element around to the front.
        A[0] = last_element

    return A

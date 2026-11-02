def solution(A, K):
    n = len(A)
    if n == 0:              # empty array, nothing to rotate
        return A

    rotated = [0] * n
    for i in range(n):
        # each element moves K spots right, wrapping around the end
        new_pos = (i + K) % n
        rotated[new_pos] = A[i]

    return rotated

def solution(A):
    n = len(A)
    # sum of 1 to n+1 using the formula k(k+1)/2 with k = n+1
    expected = (n + 1) * (n + 2) // 2

    actual = 0
    for num in A:
        actual = actual + num

    # whatever is missing from the sum is the missing number
    return expected - actual

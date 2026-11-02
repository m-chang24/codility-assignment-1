def solution(A):
    seen = set()
    for num in A:
        if num > 0:            # only positive numbers matter
            seen.add(num)

    smallest = 1
    while smallest in seen:    # count up until we find a gap
        smallest = smallest + 1

    return smallest

def solution(X, Y, D):
    distance = Y - X
    jumps = distance // D      # full jumps that fit

    if distance % D != 0:      # leftover distance needs one more jump
        jumps = jumps + 1

    return jumps

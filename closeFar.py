# Given three ints, a b c, return True if one of b or c is "close" (differing from
# a by at most 1), while the other is "far", differing from both other values by 2 or
# more. Note: abs(num) computes the absolute value of a number.
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True
# close_far(4, 5, 3)  →  False


def close_far(a, b, c):
    resa = a - b
    resa = abs(resa)

    resb = b - c
    resb = abs(resb)

    resc = a - c
    resc = abs(resc)

    if resa == 1 or resa == 0:
        if abs(c - b) >= 2 and abs(c - a) >= 2:
            return True
    elif resb == 1 or resb == 0:
        if abs(a - b) >= 2 and abs(a - c) >= 2:
            return True
    elif resc == 1 or resc == 0:
        if abs(b - a) >= 2 and abs(b - c) >= 2:
            return True
    return False


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
print(close_far(4, 5, 3))
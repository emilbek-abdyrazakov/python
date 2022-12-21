# Given three ints, a b c, return True if one of b or c is "close" (differing from
# a by at most 1), while the other is "far", differing from both other values by 2 or
# more. Note: abs(num) computes the absolute value of a number.
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True
# close_far(4, 5, 3)  →  False


def close_far(a, b, c):
    resc = b - c
    resc = abs(resc)

    resa = a - b
    resa = abs(resa)

    resb = a - c
    resb = abs(resb)

    if resa == 1 or resb == 1:
        if c - b - a > 2:
            return True
    return False


print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
print(close_far(4, 5, 3))
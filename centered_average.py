# Return the "centered" average of an array of ints, which we ll
# say is the mean average of the values, except ignoring the largest and
# smallest values in the array. If there are multiple copies of the smallest
# value, ignore just one copy, and likewise for the largest value. Use int
# division to produce the final average. You may assume that the array is
# length 3 or more.
# SOLVED
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    res = 0
    helper = len(nums)-2
    sort = sorted(nums)
    for i in range(1, len(sort) - 1):
        res += sort[i]
    res = res // helper
    return res


print(centered_average([1, 1, 5, 5, 10, 8, 7]))

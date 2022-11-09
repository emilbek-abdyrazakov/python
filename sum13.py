# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers
# that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6
def sum13(nums):
    summa = 0
    if len(nums) < 1:
        return 0
    if nums[-1] == 13:
        nums[-1] = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            nums[i + 1] = 0
        summa += nums[i]
    return summa


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))
print(sum13([13, 0, 13]))
print(sum13([5, 13, 2]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([13]))
print(sum13([]))
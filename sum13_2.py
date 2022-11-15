def sum13_2(nums):
    summa = 0
    for i in range(len(nums)):
        if nums[i] != 13 and (nums[i - 1] != 13 or i == 0):
            summa += nums[i]
    return summa


print(sum13_2([1, 2, 2, 1]))
print(sum13_2([1, 2, 2, 1, 13]))
print(sum13_2([13, 0, 13]))
print(sum13_2([5, 13, 2]))
print(sum13_2([13, 1, 2, 13, 2, 1, 13]))
print(sum13_2([13]))
print(sum13_2([]))
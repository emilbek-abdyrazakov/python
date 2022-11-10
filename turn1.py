def turn1(nums):
    for i in range(len(nums)):
        if nums[i] != 1:
            nums[i] = 1
    return nums


print(turn1([1, 9, 9, 3, 9]))
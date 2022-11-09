def bubble_optimized(nums):
    iteration = 0
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                iteration += 1
    return nums, iteration


print(bubble_optimized([9, 8, 7, 6, 5, 4, 3, 2, 1]))

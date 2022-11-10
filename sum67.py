# Return the sum of the numbers in the array, except ignore sections of
# numbers starting with a 6 and extending to the next 7 (every 6 will be
# followed by at least one 7). Return 0 for no numbers.
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    count = 0
    i = 0
    switch = 0
    if len(nums) == 0:
        count = 0
    else:
        while i < len(nums):
            if nums[i] != 6 and switch == 0 and nums[i] != 7:
                count += nums[i]
                i += 1
                # print("incremented")
                continue
            if nums[i] == 6 and switch == 0:
                switch = 1
                # print("switch ON")
                i += 1
            if nums[i] == 6 and switch == 1:
                i += 1
            if nums[i] == 7 and switch == 0:
                count += nums[i]
                # print("again 7")
                i += 1
            if switch == 1 and nums[i] == 7:
                switch = 0
                # print("switch OFF")
                i += 1
            else:
                i += 1
    # print(count)
    return count


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))

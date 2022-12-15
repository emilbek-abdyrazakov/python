# Return the sum of the numbers in the array, except ignore sections of
# numbers starting with a 6 and extending to the next 7 (every 6 will be
# followed by at least one 7). Return 0 for no numbers.
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    sum = 0
    switch = 0
    for i in nums:
        if i != 6 and switch == 0:
            sum += i
        if i == 6 and switch == 0:
            switch = 1
        if i == 7 and switch == 1:
            switch = 0
    return sum


print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))

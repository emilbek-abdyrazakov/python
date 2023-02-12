def splittting(start, n):
    result = []
    # if start % 2 == 0:
    #     result.append(start)
    # else:
    #     result.append(start+1)
    # for i in range(0, n-1):
    #     result.append(result[i]+2)  # [2] => [2, 4] => [2, 4, 6] =>
    # return result
    for i in range(0, n):
        if len(result) == 0:
            result.append(start)
        else:
            result.append(result[i - 1] + 2)
    return result


print(splittting(2, 4))
print(splittting(5, 3))

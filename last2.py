# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):
    b = str[-2:]
    counter = 0
    for i in range(len(str)-3):
        if str[i] + str[i+1] == b:
            counter+=1
    return counter


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
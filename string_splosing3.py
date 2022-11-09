# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'
def string_splosion(str):
    b=""
    for i in range(len(str)+1):
        b = b + str[:i]
        print(b)


print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
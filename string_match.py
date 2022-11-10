# Given 2 strings, a and b, return the number of the positions where
# they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
# yields 3, since the "xx", "aa", and "az" substrings appear in the
# same place in both strings.
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0
# string_match('h', 'hello') → 0
# string_match('aabbccdd', 'abbbxxd') → 1
# string_match('iaxxai', 'aaxxaaxx') → 3
def string_match(a, b):
    short = a
    long = b
    if len(long) < len(a):
        long = a
    if len(short) > len(b):
        short = b
    counter = 0
    for i in range(len(short) - 1):
        if long[i] + long[i + 1] == short[i] + short[i + 1]:
            counter += 1
    return counter


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match('h', 'hello'))
print(string_match('aabbccdd', 'abbbxxd'))
print(string_match('iaxxai', 'aaxxaaxx'))

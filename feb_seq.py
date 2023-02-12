# fib_cache = {}
# def fibseq(n):
#     if n in fib_cache:
#         return fib_cache[n]
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value =  (fibseq(n-1)+ (fibseq(n-2)))
#     fib_cache[n] = value
#     return value
#
# for i in range(1,6):
#     print(fibseq(i))

# def fibseq(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibseq(n-1) + fibseq(n-2)
#
# print(fibseq(4))

def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(6))
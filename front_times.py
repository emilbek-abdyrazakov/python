# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'
# front_times('Ab', 4) → 'AbAbAbAb'
def front_times(str, n):
    if len(str) < 3:
        return str*n
    return str[:3]*n


print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))
print(front_times('Ab', 4))
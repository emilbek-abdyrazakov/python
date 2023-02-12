def paper_doll(text):
    res = ""
    for i in text:
        res = res + i * 3
    return res


print(paper_doll("Hello"))
print(paper_doll("Mississippi"))
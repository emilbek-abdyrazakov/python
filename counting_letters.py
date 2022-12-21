import string


def counting_letters(s):
    s = s.lower().strip()
    s = s.strip(string.punctuation)
    list1 = list(s)
    letters = {}
    for i in list1:
        if i.isalpha():
            if i in letters:
                letters[i]+=1
            else:
                letters[i] = 1
    return letters
    # return(sorted(letters.items(), key=lambda x: x[1], reverse=True)[0])


print(counting_letters("But is this what it feels like To be growing apart? When did I become the one Who's always chasing your heart?"))
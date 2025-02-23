import re
#task 1
with open('row1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        lines = line.split()
        for word in lines:
            if re.fullmatch(r"ab*$", word):
                print(word)

#task 2
pat = r"ab{2,3}$"
with open('row1.txt','r', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            if re.fullmatch(pat, word):
                print(word)

#task 3
with open('row.txt', 'r') as ok:
    pat = r"^[a-z]+(?:_[a-z]+)+"
    for lines in ok:
        words = lines.split()
        for word in words:
            if re.fullmatch(pat, word):
                print(word)

#task 4


with open('row.txt', 'r') as ok:
    pat = r"^[A-Z][a-z]+$"
    for lines in ok:
        words = lines.split()
        for word in words:
            if re.fullmatch(pat, word):
                print(word)

#task 5


with open('row.txt', 'r') as ok:
    pat = r"^a.*b$"
    for lines in ok.readlines():
        words = lines.split()
        for word in words:
            if re.fullmatch(pat, word):
                print(word)

#task 6


with open('row.txt', 'r') as ok:
    for lines in ok.readlines():  
        pat = re.sub(r"[ ,.]", ":", lines)
        print(pat)


#task 7


with open('row.txt', 'r') as ok:
    for line in ok.readlines():
        pat = re.sub(r"snake", "camel", line)
        print(pat)

#task 8


with open('row.txt', 'r') as ok:
    for lines in ok.readlines():
        pat = re.sub(r"(?=[A-ZА-Я])", "...", lines).strip()
        print(pat)

#task 9


with open('row.txt', 'r') as ok:
    for lines in ok.readlines():
        pat = re.sub(r"(?=[A-ZА-Я])", ' ', lines).strip()
        print(pat)


#task 10


with open('row.txt', 'r') as ok:
    for lines in ok.readlines():
        pat = re.sub(r"camel", "snake", lines)
        print(pat)
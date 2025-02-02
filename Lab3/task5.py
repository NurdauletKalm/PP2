def reversedlist(s):
    return s[::-1]
sentence = list(map(str, input().split()))
rs = reversedlist(sentence)
print(rs)

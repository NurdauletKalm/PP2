def solve(heads, legs):
    for i in range(heads + 1):
        j = heads - i
        if 2 * j + 4 * i == legs:
            return i, j
heads = int(input("қанша басы?:"))
legs = int(input("қанша аяғы?:"))
print(solve(heads, legs))
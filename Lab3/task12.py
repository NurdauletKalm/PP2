def histogram(n):
    for i in n:
        print(i * "*")
nums = list(map(int, input().split()))
histogram(nums)
def check_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return n
    elif n%2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return n
    
num = list(map(int, input().split()))
for i in num:
  if(check_prime(num[i])) != 0:
      print(num[i])
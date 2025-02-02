def palindrome(n):
    r = n[::-1]
    if(r == n):
        print("palindrome")
    else:
        print("not")
s = input()
palindrome(s)
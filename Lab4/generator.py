# Create a generator that generates the squares of numbers up to some number N.

# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

# Implement a generator that returns all numbers from (n) down to 0.

# def count(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# gen = count(3)
# print(next(gen))
# print(next(gen))
# print(next(gen))

#task 1
def sq_up_to(n):
    counter = 1
    while counter <= n:
        yield counter ** 2
        counter += 1
n = int(input())
gen = sq_up_to(n)
for _ in range(n):
    print(next(gen), end = " ")


#task 2
def even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i
n = int(input())
print(', '.join(map(str, list(even(n)))))


#task 3
def divis(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i
n = int(input())
print(' '.join(map(str, list(divis(n)))))

#task 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

#a, b = map(int, input().split())
a, b = int(input()), int(input())
for i in squares(a, b):
    print(i, end = ' ')

#task 5

def down(n):
    for i in range (n, -1, -1):
        yield i
n = int(input())
gen = down(n)
for _ in range(n):
    print(next(gen), end = " ")
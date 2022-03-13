def squares(n):
    for i in range(n):
        yield i**2

n = int(input())
for j in squares(n):
    print(j)
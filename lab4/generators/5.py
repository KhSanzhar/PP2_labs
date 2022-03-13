def dec(n):
    for i in range(n, -1, -1):
        yield i

x = int(input())
for i in dec(x):
    print(i, end = ' ')
def squares(a, b):
    for i in range(a, b):
        yield i**2
    
a,b = map(int, input().split())
for i in squares(a,b):
    print(i, end = ' ')
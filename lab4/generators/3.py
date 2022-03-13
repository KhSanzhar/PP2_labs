def nums(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

x = int(input())
for i in nums(x):
    print(i)
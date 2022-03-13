def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input())
evens_row = []
for j in evens(n):
    evens_row.append(str(j))

print(', '.join(evens_row))

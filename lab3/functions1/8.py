def game(nums):
    n = []
    for i in nums:
        if i == 0 or i == 7:
            n.append(i)
    if n[0] == n[1] == 0 and n[2] == 7:
        return True
    return False

nums = list(map(int, input().split()))
print(game(nums))
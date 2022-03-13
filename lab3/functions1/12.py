
def histogramm(list):
    dubl = []
    h = []
    for i in list:
        for j in range(i):
            dubl.append('*')
        h.append(dubl)
    print(h, sep = ',')

n = list(map(int, input().split()))
histogramm(n)
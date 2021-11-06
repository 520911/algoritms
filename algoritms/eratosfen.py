n = int(input('Количество чисел: '))
siev = [i for i in range(n)]
siev[1] = 0

for i in range(2, n):
    if siev[i] != 0:
        j = i * 2
        while j < n:
            siev[j] = 0
            j += i

result = [i for i in siev if i != 0]
print(result)

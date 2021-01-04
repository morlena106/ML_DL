from math import sqrt

gs = [float(i) for i in input().split()]

raspr = {}
for i in gs:
    if i in raspr.keys():
        raspr[i] += 1
    else:
        raspr[i] = 1

m = max(raspr.values())
for i in raspr.keys():
    if raspr[i] == m:
        mode = i

X = sum(gs) / len(gs)

Range = max(gs) - min(gs)

D = 0

for i in gs:
    D += (i - X) ** 2
D = D / (len(gs) - 1)

sd = sqrt(D)

print(f'Мода {mode}')
print(f'Среднее значение {X}')
print(f'Размах {Range}')
print(f'Дисперсия {D}')
print(f'Стандартное отклонение {sd}')

a = 7
b = 1
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')

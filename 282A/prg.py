n = int(input())
x = 0
for k in range(0, n):
    o = input()
    if '++' in o:
        x += 1
    else:
        x -= 1
print(x)
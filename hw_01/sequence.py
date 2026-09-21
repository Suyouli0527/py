n = int(input())

a = 1
b = 1
total = 0
for i in range(n):
    total = total + a
    n = a
    a = b
    b = n + b

print(total)

n = int(input())
total = 0
for five in range(n//5, -1, -1):
    three = n - (five * 5)
    if three % 3 == 0:
        total = five + three // 3
        break
else:
    print(-1)
    exit()

print(total)
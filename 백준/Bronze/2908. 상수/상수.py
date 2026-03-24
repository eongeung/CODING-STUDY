a, b = input().split()
ra, rb = int(a[::-1]), int(b[::-1])
print(a[::-1] if ra > rb else b[::-1])
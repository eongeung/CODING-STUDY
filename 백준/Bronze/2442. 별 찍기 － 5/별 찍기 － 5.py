n = int(input())
for i in range(n):
    stars = 2 * i + 1
    spaces = n - i - 1
    print(" " * spaces + "*" * stars)
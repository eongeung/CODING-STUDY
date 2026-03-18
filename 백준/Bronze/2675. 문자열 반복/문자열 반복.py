t = int(input())
for i in range(t):
    r,s = input().split()
    print("".join(c * int(r) for c in s))
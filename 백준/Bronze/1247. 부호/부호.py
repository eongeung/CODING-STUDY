for i in range(3):
    n = int(input())
    s = sum(int(input()) for j in range(n))
    print("+" if s > 0 else "-" if s < 0 else "0")
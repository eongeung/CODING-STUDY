a,b = map(int,input().split())
c = int(input())

total = b + c
hour = a + total // 60
minute = total % 60

print(hour % 24, minute)
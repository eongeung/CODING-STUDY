n = int(input())
numbers = list(map(int, input().split()))

min_value = numbers[0]
max_value = numbers[0]

for i in range(n):
    if numbers[i] < min_value:
        min_value = numbers[i]
    if numbers[i] > max_value:
        max_value = numbers[i]
        
print(min_value, max_value)
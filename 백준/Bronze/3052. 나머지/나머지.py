numbers = []
for i in range(10):
    n = int(input())
    numbers.append(n)
total = []
for i in range(10):
    result = numbers[i] % 42
    total.append(result)  
b = set(total)
print(len(b))
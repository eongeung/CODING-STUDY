numbers=[]
for i in range(9):
    numbers.append(int(input()))
max_value = numbers[0]
index = 0

for i in range(9):
    if max_value < numbers[i]:
        max_value = numbers[i]
        index = i
        
print(max_value)
print(index+1)
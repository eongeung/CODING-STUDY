submit = []

for i in range(28):
    n = int(input())
    submit.append(n)
   
count = 0
for i in range(1, 31):
    if i not in submit:
        print(i)
        count+=1
    if count ==2:
        break
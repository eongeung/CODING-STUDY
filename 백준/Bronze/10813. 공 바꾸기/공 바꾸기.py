n, m = map(int, input().split())
basket = list(range(n+1))
           
for i in range(m):
    k, j = map(int, input().split())
    basket[k], basket[j] = basket[j], basket[k]
            
for l in range(1, n+1):
    print(basket[l], end=' ')           
  
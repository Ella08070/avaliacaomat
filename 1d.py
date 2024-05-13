def P(n):
  if n == 1:
      return 1
  else:
      return (n*n)+ P(n - 1) + n


#Testa pra valor n
for i in range(1, 6):
  print(f"P({i}) = {P(i)}")

def B(n):
  if n == 1:
      return 1
  else:
      return B(n - 1) + (n * n)


#Testa pra valor n
for i in range(1, 6):
  print(f"B({i}) = {B(i)}")

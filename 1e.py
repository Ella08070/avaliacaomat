def D(n):
  if n == 1:
      return 3
  elif n == 2:
      return 5
  else:
      return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

#Testa pra valor n
for n in range(1, 11):
  print(f"D({n}) = {D(n)}")

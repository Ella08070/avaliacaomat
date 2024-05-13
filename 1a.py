def S(n):
  if n == 1:
      return 10
  else:
      return S(n - 1) + 10

# Testa pra valor n
for i in range(1, 6):
  print(f"S({i}) = {S(i)}")

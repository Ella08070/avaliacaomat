def colecao3(n):
  if n == 2:
      return True
  elif n < 2:
      return False
  else:
      return colecao3(n - 3) or colecao3(n // 2)

valores = [6, 7, 19, 12]
for n in valores:
  if colecao3(n):
      print(f"O número {n} pertence a T")
  else:
      print(f"O número {n} não pertence a T")

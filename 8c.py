def s(n, a, b):
  if n == 1:  # Se n = 1, retorna primeiro da sequência, a
      return a
  elif n == 2:  # Se n = 2, retorna segundo da sequência, b
      return b
  else:
      return a + (n - 1) * b + s(n - 2, a, b)

# Teste
n = 6
a = 1
b = 2
resultado = s(n, a, b)
print(f'O valor de S({n}) é: {resultado}')

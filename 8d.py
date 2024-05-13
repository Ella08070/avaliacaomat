def s(n, p, q):
  if n == 1:  # Se n = 1, retorna o primeiro da sequência, p
      return p
  elif n == 2:  # Se n = 2, retorna o segundo  da sequência, p-q
      return p - q
  else:
      if n % 2 == 0:  # Se n = par, sinal negativo
          return p - ((n // 2) * q) + s(n - 1, p, q)
      else:  # Se n = ímpar, sinal positivo
          return p + (((n + 1) // 2) * q) + s(n - 1, p, q)

# Teste
n = 3
p = 6
q = 2
resultado = s(n, p, q)
print(f'O valor de S({n}) é: {resultado}')

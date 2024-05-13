def pitagoras(n):
  if n == 1:
      return 1
  else:
      return n + pitagoras(n - 1)

# Testa com o quarto número triangular
n = 4
print(f"O {n}-ésimo número triangular é {pitagoras(n)}")

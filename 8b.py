def s(n, a, b):
  if n == 1:
      return a
  elif n == 2:
      return s(n - 2, a, b) + (n - 1) * b
  else:
      return s(n - 2, a, b) + (n - 1) * b

a = 1
b = 1
for i in range(1, 6):
  print(f"S{i}={s(i, a, b)}")

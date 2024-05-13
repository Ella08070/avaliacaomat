def s(n):
  if n == 1:
      return 1
  else:
      return 3 * s(n - 1)

for i in range(1, 6):
  print(f"S{i}={s(i)}")

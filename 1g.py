def T(n):
    if n == 1:
      return 1
    elif n == 2:
      return 2
    elif n == 3:
        return 3
    else:
      return T(n - 1) + 2 * T(n - 2) + 3 *  (n - 3)

#Testa pra valor n
for n in range(1, 11):
  print(f"T({n}) = {T(n)}")

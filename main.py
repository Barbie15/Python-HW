def f(x, n):
  if x == n:
    return 1
  elif x > n or x == 43:
    return 0
  elif x < n :
    return f(x + 3, n) + f(x * 3, n)
print (f(7, 63))
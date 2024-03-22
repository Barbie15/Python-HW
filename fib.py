def fib(x):
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fib(x - 1) + fib(x - 2)


x1 = 1
x2 = 0
res = 0
n = int(input())
for x in range(n):
  res = x1 + x2
  x2 = x1
  x1 = res


print(x2)
print(fib(n))
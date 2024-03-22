def pluse_1(x):
    i = 1
    trigger = 0
    size = len(x)
    while (i <= size):
      if x[-i] == 9:
        x[-i] = 0
        i += 1
        trigger = 1
      else:
        x[-i] += 1
        trigger = 0
    if trigger == 1:
      a = [1]
      a.extend(x)
      return a
    else:
      return x


print(pluse_1([9, 9, 9]))


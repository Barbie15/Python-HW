def check(m, arr):
    for index1, value1 in enumerate(arr[:-1]):
        for index2, value2 in enumerate(arr[index1 + 1:]):
            if index1 != index2 and (value1 + value2) == m:
                print(value1, value2)

check(9,[2, 7, 11, 15])
def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(add(2, 6, 18, 15, 206, 358, 106, 1024))

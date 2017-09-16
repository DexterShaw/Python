def s(i):
    print('zaczynam z liczbą', i)
    if i == 0:
        result = 1
    else:
        result = i * s(i - 1)
    print('kończę z liczbą', i)
    return result

def f(i):
    if i in [0, 1]:
        return
    else:
        return f(i - 1) + f(i - 2)


def f(i):
    print('zaczynam z liczbą', i)
    if i in [0, 1]:
        result = 1
    else:
        result = f(i - 1) + f(i - 2)
    print('kończę i liczbą', i)
    return result

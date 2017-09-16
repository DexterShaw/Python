def h(n, source, target, helping):
    if n > 0:
        h(n - 1, source, helping, target)
        print('przenoszę klocek rozmiaru', n, 'z', source, 'na', target)
        h(n - 1, helping, target, source)


h(64, 'A', 'B', 'C')
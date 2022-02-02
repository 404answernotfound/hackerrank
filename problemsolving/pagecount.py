def pageCount(n, p):
    if p > n//2:
        if n - p == 1 and n % 2 == 0:
            return 1
        return int((n - p) * 0.5)
    else:
        return int(p * 0.5)
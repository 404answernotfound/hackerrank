def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    socks = {}
    pairs = 0
    for i, val in enumerate(ar):
        socks[val] = 0
    for val in ar:
        socks[val] += 1
    for i in socks:
        if socks[i] % 2 == 0:
            pairs += socks[i] / 2 
        elif socks[i] % 2 == 1:
            pairs += (socks[i] - 1) / 2
        else:
            pairs += 0
    return math.floor(pairs)
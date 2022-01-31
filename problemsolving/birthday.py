def birthday(s, d, m):
    # Write your code here
    #1 2 1 3 2 - 3 2
    ss = 0
    t = 0
    counter = 0
    if len(s) == 1 and m != 1 or m == 0:
        return 0

    for i, val in enumerate(s):
        for j in range(m):
            counter += 1
            j += i
            ss += s[j]
            if ss == d and counter == m:
                t += 1
        ss = 0
        counter = 0
        if i == len(s) - m:
            break           
    return t
def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    occurances = {}
    t, tid, pid = -1, 0, 6
    for i in arr:
        if i in occurances:
            occurances[i] += 1
        else:
            occurances[i] = 1
    for i in occurances:
        if occurances[i] > t:
            t = occurances[i]
            tid = i
        if occurances[i] == t:
            if i < tid:
                tid = i
    return tid
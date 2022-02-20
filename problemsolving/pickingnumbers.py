def pickingNumbers(a):
    # Solution not implemented by me
    result = 0
    checked = set()
    for i in range(len(a)):
        if i not in checked:
            maxCount = max(a.count(a[i]) + a.count(a[i] + 1), a.count(a[i]) + a.count(a[i] - 1))
            if maxCount > result:
                result = maxCount
            checked.add(i)
    return result
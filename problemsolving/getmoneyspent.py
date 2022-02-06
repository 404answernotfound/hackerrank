def getMoneySpent(keyboards, drives, b):
    highb = 0
    for i in keyboards:
        for j in drives:
            if i + j > highb and i + j <= b:
                highb = i + j
    if highb == 0:
        return -1
    return highb

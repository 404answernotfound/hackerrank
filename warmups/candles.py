def birthdayCakeCandles(candles):
    # Write your code here
    high, q = 0, 0
    print(candles)
    for value in candles:
        if value == high:
            q += 1
        if value > high:
            high = value
            q = 1
    return q
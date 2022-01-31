def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    _a, _o = [], []
    _ap, _ot = 0, 0
    for fruit in apples:
        if a + fruit >= s and a + fruit <= t:
            _ap += 1
    for fruit in oranges:
        if b + fruit >= s and b + fruit <= t:
            _ot += 1
    print(_ap)
    print(_ot)

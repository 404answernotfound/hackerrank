def plusMinus(arr):
    # Write your code here
    l = len(arr)
    r = [0, 0, 0]
    
    for i in arr:
        if i > 0: r[0] += 1
        if i < 0: r[1] += 1
        elif i == 0: r[2] += 1
        
    for i in r:
        print(round(i/l, 6))
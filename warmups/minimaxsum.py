def miniMaxSum(arr):
    # Write your code here
    minval = arr[0]
    maxval = 0
    minpos = 0
    maxpos = 0
    minsum = 0
    maxsum = 0
    
    for i in range(len(arr)):
        if arr[i] >= maxval:
            maxval = arr[i]
            maxpos = i
        if arr[i] <= minval:
            minval = arr[i]
            minpos = i
        
    for i in range(len(arr)):
        if(i != maxpos): maxsum += arr[i]
        if(i != minpos): minsum += arr[i]
    print(str(maxsum) + ' ' + str(minsum))
def diagonalDifference(arr):
    # Write your code here
    _abs = 0
    _sum = [0, 0]
    _start = 0
    _tail = len(arr[0]) - 1
    
    for i in range(len(arr)):
        _sum[0] += arr[i][_start]
        _sum[1] += arr[i][_tail]
        _start += 1
        _tail -= 1

    return abs(_sum[0] - _sum[1])
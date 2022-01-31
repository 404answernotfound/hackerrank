def staircase(n):
    # Write your code here
    nn = n - 1
    for i in range(n):
        print(nn * ' ' + (i + 1) * '#')
        nn -= 1
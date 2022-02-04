def countingValleys(steps, path):
    # Write your code here
    count = 0
    valleys = 0
    trailing = False
    for i in path:
        if i == 'U':
            count += 1
        else:
            count -= 1
        if count < 0 and trailing == False:
            valleys += 1
            trailing = True
        if count == 0:
            trailing = False
    return valleys
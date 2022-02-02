def bonAppetit(bill, k, b):
    # Write your code here
    realbill = 0
    for i, val in enumerate(bill):
        if i != k:
            realbill += val
    if realbill / 2 == b:
        print("Bon Appetit")
    else:
        realbill = math.floor(realbill / 2)
        print(b - realbill)

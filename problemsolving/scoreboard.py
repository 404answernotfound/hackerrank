def breakingRecords(scores):
    # Write your code here
    high, low, th, tl = 0, 0, 0, 0
    for i, score in enumerate(scores):
        if i == 0:
            high, low = score, score
        else:
            if score > high:
                th += 1
                high = score
            elif score < low:
                tl += 1
                low = score

    return [th, tl]

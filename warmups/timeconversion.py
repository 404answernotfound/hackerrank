def timeConversion(s):
    # Write your code here
    t, h = s.split(':')[2][2], s.split(':')
    if t == 'P' and h[0] != '12':
        h[0] = str(int(h[0]) + 12)
    if t == 'A' and h[0] == '12':
        h[0] = '00'
    return ':'.join(h)[0:8]
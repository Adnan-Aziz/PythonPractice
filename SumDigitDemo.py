def sumDigit(s):
    sum = 0
    for c in s :
        try:
            sum+=int(c)
        except ValueError:
            continue
    return sum

print("{0}".format(sumDigit("a12b3c")))
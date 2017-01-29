def getNumber(n, step = 1):
    i = 0
    numbers = []

    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Number now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

numbers = getNumber(6, 2)
print "The numbers: "

for num in numbers:
    print num

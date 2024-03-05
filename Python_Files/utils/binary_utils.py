import random


# this is where binary numbers are generated, n is the max length of numbers to be generated
def generateRandomBinary(n):

    # generate length of binary string (min length 4)
    # p = random.randint(4, n)

    # byte strings?
    key1 = ""

    # Loop to find the string
    # of desired length
    for i in range(n):

        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))

        key1 += temp

    return key1


# computes the 2's complement of binary numbers
def twosComp(n, size):

    # where to store converted binary
    binResult = ""

    i = size - 1
    # finding first 1
    while n[i] != "1":
        binResult = n[i] + binResult
        i -= 1

    binResult = n[i] + binResult
    i -= 1

    # flipping the rest of the bits
    while i > -1:
        if n[i] == "1":
            binResult = "0" + binResult
        else:
            binResult = "1" + binResult
        i -= 1

    return binResult


# pads binary to the correct number of bits
def binPadding(n, e):

    n = n[2:]
    toPad = e - len(n)
    i = 0
    while i < toPad:
        n = "0" + n
        i += 1
    return n

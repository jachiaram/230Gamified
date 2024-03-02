from utils import binary_utils


# binary multiplication algorithm
def multAlg(n, m):

    # lamda function to add two binary numbers together
    binarySum = lambda a, b: bin(int(a, 2) + int(b, 2))

    # generate random binary numbers to be multiplied
    multd = binary_utils.generateRandomBinary(n)
    multr = binary_utils.generateRandomBinary(m)

    # multd = "1010"
    # multr = "0100"

    # set up product string
    prod = ""
    prodLen = n + m

    # populate prod with zeros
    for i in range(prodLen):
        prod += "0"

    # bool values to check if multd and multr are 2's comp
    dComp = False
    rComp = False

    print("Use the multiplication algorithm to multiply " + multd + " and " + multr)

    # check for leading bit 1, if 2's comp numbers
    if multd[0] == "1":
        dComp = True
        multd = binary_utils.twosComp(multd, n)

    if multr[0] == "1":
        rComp = True
        multr = binary_utils.twosComp(multr, m)

    print("Initial Values: ")
    print("Multiplicand: " + multd)
    print("Multiplier: " + multr)
    print("Product: " + prod + "\n")

    size = m
    for i in range(m):
        # if ending bit is 1 add to product
        if multr[size - 1] == "1":
            prod = binarySum(prod, multd)

        # shift multd left
        multd = multd + "0"

        # shift multr right
        multr = list(multr)
        multr.pop()
        multr = "".join(multr)
        size = size - 1

        # print out current values
        print("The current multiplicand: " + multd)
        print("The current multiplier: " + multr)
        print("The current product: " + prod + "\n")

    # check length of prod string, pad to correct number of bits
    prod = prod[2:]
    curlen = len(prod)
    while curlen < prodLen:
        prod = "0" + prod
        curlen += 1

    # check for need to 2's comp the prod
    if (dComp == True and rComp == False) or (dComp == False and rComp == True):
        prod = binary_utils.twosComp(prod, prodLen)

    print("Final Product: " + prod)

    return

from utils import binary_utils


# binary division algorithm
def divAlg(n, m):
    # lamda function to add two binary numbers together
    binarySum = lambda a, b: bin(int(a, 2) + int(b, 2))
    binaryDiff = lambda a, b: bin(int(a, 2) - int(b, 2))

    dividend = binary_utils.generateRandomBinary(n)
    divisor = binary_utils.generateRandomBinary(m)
    quotient = ""

    j = 0
    while j != m and divisor[j] != "1":
        j += 1

    if j == m:
        return

    j += 1
    # bool values to check if multd and multr are 2's comp
    ddComp = False
    drComp = False

    print("Use the division algorithm to divide " + dividend + " by " + divisor)

    # check for leading bit 1, if 2's comp numbers
    if dividend[0] == "1":
        ddComp = True
        dividend = binary_utils.twosComp(dividend, n)

    if divisor[0] == "1":
        drComp = True
        divisor = binary_utils.twosComp(divisor, m)

    # right justify divisor
    for i in range(m):
        divisor = divisor + "0"

    # setting the new size of divisor
    m *= 2

    print("Initial Values: ")
    print("Divisor: " + divisor)
    print("Remainder (Dividend): " + dividend)
    print("Quotient: " + quotient + "\n")

    size = m
    j = m - j
    # algo loop
    for i in range(j):

        # remainder = remainder - divisor
        dividend = binaryDiff(dividend, divisor)

        # cond dividend[0] == '1'
        if dividend[0] == "-":
            # rem += divisor
            dividend = binarySum(dividend, divisor)
            quotient += "0"
        else:
            quotient += "1"

        # shift divisor right
        divisor = list(divisor)
        divisor.pop()
        divisor = "".join(divisor)
        size = size - 1

        # print out current values
        print("The current divisor: " + divisor)
        print("The current remainder: " + dividend)
        print("The current quotient: " + quotient + "\n")

    print("Final Quotient: " + quotient)
    print("Final Remainder: " + dividend)

    return

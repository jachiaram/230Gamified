from utils import binary_utils
from utils import quiz_prompter as prompt
from types import SimpleNamespace


questionNames = ["Multiplicand", "Multiplier ", "Product: "]
problemVals = SimpleNamespace(promptString="", expectedValue="")
maxAttempts = 5
attempts = 0

def multiplicationPrompt(multd, multr):
    initial_prompt = ("Use the multiplication algorithm "
                      + "to multiply " + multd + " and " + multr)
    print(initial_prompt)
def binarySum(a, b):
    # lamda function to add two binary numbers together
    sum = bin(int(a, 2) + int(b, 2))
    print("binarySum function Call:::::" + sum)
    return sum

# binary multiplication algorithm
def multAlg(n, m):
    global attempts
    attempts = 0

    # generate random binary numbers to be multiplied
    multd = binary_utils.generateRandomBinary(n)
    multr = binary_utils.generateRandomBinary(m)

    # set up product string
    prod = ""
    prodLen = n + m
    # populate prod with zeros
    for i in range(prodLen):
        prod += "0"

    questionVals = [multd, multr, prod]

    # bool values to check if multd and multr are 2's comp
    dComp = False
    rComp = False

    multiplicationPrompt(multd, multr)

    # check for leading bit 1, if 2's comp numbers
    if questionVals[0][0] == "1":
        dComp = True
        questionVals[0] = binary_utils.twosComp(questionVals[0], n)

    if questionVals[1][0] == "1":
        rComp = True
        questionVals[1] = binary_utils.twosComp(questionVals[1], m)

    for i in range(3):
        if attempts >= maxAttempts:
            return False
        problemVals.promptString = questionNames[i]
        problemVals.expectedValue = questionVals[i]
        if not prompt.answerLoop(problemVals.promptString, problemVals.expectedValue):
            attempts += 1
    # print("Multiplier: " + multr)
    # print("Product: " + prod + "\n")

    size = m
    for i in range(m):
        # if ending bit is 1 add multiplicand to product
        if questionVals[1][size - 1] == "1":
            tempStr = binarySum(questionVals[2], questionVals[0])
            questionVals[2] = tempStr[2:]  # removes 0b

        curlen = len(questionVals[2])
        while curlen < prodLen:
            questionVals[2] = "0" + questionVals[2]
            curlen += 1

        # shift multd left
        questionVals[0] += "0"

        # shift multr right

        shiftString = ("0" + questionVals[1])
        questionVals[1] = shiftString[:-1]
        # multr = list(multr)
        # multr.pop()
        # multr = "".join(multr)
        size = size - 1
        for i in range(3):
            if attempts >= maxAttempts:
                return False
            problemVals.promptString = questionNames[i]
            problemVals.expectedValue = questionVals[i]
            if not prompt.answerLoop(problemVals.promptString, problemVals.expectedValue):
                attempts += 1

    # check for need to 2's comp the prod
    if dComp and not rComp or not dComp and rComp:
        prod = binary_utils.twosComp(prod, prodLen)

    print("Final Product: " + questionVals[2])

    return True

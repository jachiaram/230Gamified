import random



#this is where binary numbers are generated, n is the max length of numbers to be generated
def generateRandomBinary(n):
    
    #generate length of binary string (min length 4)
    #p = random.randint(4, n)

    #byte strings?
    key1 = ""
 
    # Loop to find the string
    # of desired length
    for i in range(n):
         
        # randint function to generate
        # 0, 1 randomly and converting 
        # the result into str
        temp = str(random.randint(0, 1))
 
        key1 += temp
         
    return(key1)

def twosComp(n , size):
    
    binResult = ""
    
    i = size - 1
    while n[i] != '1':
        binResult = n[i] + binResult
        i -= 1

    binResult = n[i] + binResult
    i -= 1

    while i > -1:
        if n[i] == '1':
            binResult = '0' + binResult
        else:
            binResult = '1' + binResult
        i -= 1

    return binResult

#binary multiplication algorithm
def multAlg(n, m):

    #lamda function to add two binary numbers together
    binarySum = lambda a,b : bin(int(a, 2) + int(b, 2))

    #generate random binary numbers to be multiplied    
    multd = generateRandomBinary(n)
    multr = generateRandomBinary(m)
    
    # multd = "1010"
    # multr = "0100"

    #set up product string
    prod = ""
    prodLen = n + m;

    #populate prod with zeros
    for i in range(prodLen):
        prod += "0"

    #bool values to check if multd and multr are 2's comp
    dComp = False
    rComp = False
        
    print("Use the multiplication algorithm to multiply " + multd + " and " + multr )

    #check for leading bit 1, if 2's comp numbers
    if multd[0] == '1':
        dComp = True
        multd = twosComp(multd, n)

    if multr[0] == '1':
        rComp = True
        multr = twosComp(multr, m)


    print("Initial Values: ")
    print("Multiplicand: " + multd)
    print("Multiplier: " + multr)
    print("Product: " + prod + "\n")

    size = m
    for i in range(m):
        #if ending bit is 1 add to product
        if multr[size - 1] == '1':
            prod = binarySum(prod, multd)

        #shift multd left
        multd = multd + "0" 

        #shift multr right        
        multr=list(multr)
        multr.pop()
        multr="".join(multr)
        size = size - 1
        
        #print out current values
        print("The current multiplicand: " + multd)
        print("The current multiplier: " + multr)
        print("The current product: " + prod  + "\n")
    
    #check length of prod string, pad to correct number of bits
    prod = prod[2:]
    curlen = len(prod)
    while curlen < prodLen:
        prod = "0" + prod 
        curlen += 1

    #check for need to 2's comp the prod
    if (dComp == True and rComp == False) or (dComp == False and rComp == True):
        prod = twosComp(prod, prodLen) 

    print("Final Product: " + prod)
    return

#binary division algorithm
def divAlg(n, m):
    return

class MipsInstruct:
    functType = ''
    opcode = ""
    mnemonic = ""
    #this should always follow this order rd, rs, rt
    registers = ["","",""]
    shamt = ""
    funct = ""
    imm = ""

#basic machine to mips game
def machToMips():
    #define dictionaries for different parts of mip instructions to be translated
    #dictionary instrType = list out all possible for core instr set
    # i.e. 
    #dictionary registers = pair all registers to corresponding number
    #dictionary mnemonics = this should be fed into from instr type dict

    #define a function that will be able to choose a random value in a dictionary
    #choose random value for 
    return



multAlg(4, 4)
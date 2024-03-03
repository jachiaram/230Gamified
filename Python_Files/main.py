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

#computes the 2's complement of binary numbers
def twosComp(n , size):
    
    #where to store converted binary
    binResult = ""
    
    i = size - 1
    #finding first 1
    while n[i] != '1':
        binResult = n[i] + binResult
        i -= 1

    binResult = n[i] + binResult
    i -= 1

    #flipping the rest of the bits
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
    #lamda function to add two binary numbers together
    binarySum = lambda a,b : bin(int(a, 2) + int(b, 2))
    binaryDiff = lambda a,b : bin(int(a, 2) - int(b, 2))

    dividend = generateRandomBinary(n)
    divisor = generateRandomBinary(m)
    quotient = ""
    
    j = 0
    while j != m and divisor[j] != '1':
        j += 1 

    if j == m:
        return

    j += 1
    #bool values to check if multd and multr are 2's comp
    ddComp = False
    drComp = False
        
    print("Use the division algorithm to divide " + dividend + " by " + divisor)

    #check for leading bit 1, if 2's comp numbers
    if dividend[0] == '1':
        ddComp = True
        dividend = twosComp(dividend, n)

    if divisor[0] == '1':
        drComp = True
        divisor = twosComp(divisor, m)

    # right justify divisor
    for i in range(m):
        divisor = divisor + "0"

    #setting the new size of divisor
    m *= 2

    print("Initial Values: ")
    print("Divisor: " + divisor)
    print("Remainder (Dividend): " + dividend)
    print("Quotient: " + quotient + "\n")

    size = m
    j = m - j
    #algo loop
    for i in range(j):
        
        # remainder = remainder - divisor
        dividend = binaryDiff(dividend, divisor)
        
        #cond dividend[0] == '1'
        if dividend[0] == "-":
            #rem += divisor
            dividend = binarySum(dividend, divisor)
            quotient += "0"
        else:
            quotient += "1"
        
        #shift divisor right        
        divisor=list(divisor)
        divisor.pop()
        divisor="".join(divisor)
        size = size - 1
        
        #print out current values
        print("The current divisor: " + divisor)
        print("The current remainder: " + dividend)
        print("The current quotient: " + quotient  + "\n")

    print("Final Quotient: " + quotient)
    print("Final Remainder: " + dividend)
    
    return

#pads binary to the correct number of bits
def binPadding(n, e):
    
    n = n[2:]
    toPad = e - len(n)
    i = 0
    while i < toPad:
        n = "0" + n
        i += 1
    return n

#basic machine to mips game
def machToMips():
 
    registers = ["$zero", "$at", "$v0", "$v1", "$a0", "$a1", "$a2", "$a3", "$t0", "$t1", "$t2", "$t3", "$t4", "$t5", "$t6", "$t7", "$s0", "$s1", "$s2", "$s3", "$s4", "$s5", "$s6", "$s7", "$t8", "$t9", "$k0", "$k1", "$gp", "$sp", "$fp", "$ra"]
    
    #TODO: Need to fix this 
    #First choose R,I, or J at random
    # types = ["R", "I", "J"]
    # selected = random.randint(0, 3)
    # print("Selected instruction type: ", types[selected])
    #split into 3 branches

    #Randomly choose the opcode/ funct code from list (should have opcode, type, and mnemonic at this point)
    r = {0x20:"add", 0x21:"addu", 0x24:"and", 0x08:"jr", 0x27:"nor", 0x25:"or", 0x2a:"slt", 0x2b:"sltu", 0x00:"sll", 0x02:"srl", 0x22:"sub", 0x23:"subu"}
    i = {0x8:"addi", 0x9:"addiu", 0xc:"andi", 0x4:"beq", 0x5:"bne", 0x24:"lbu", 0x25:"lhu", 0x30:"ll", 0xf:"lui", 0x23:"lw", 0xd:"ori", 0xa:"slti", 0xb:"sltiu", 0x28:"sb", 0x38:"sc", 0x29:"sh", 0x2b:"sw"}
    j = {0x2:"j", 0x3:"jal"}
    
    #Randomly choose registers from the register dict, different flows for different instructions
    funct, mnemonic = random.choice(list(r.items()))
    opcode = 0x0
    shamt = 0x0
    print("Randomly selected ", hex(funct), mnemonic)
    
    #TODO: Handle special cases (sll, srl, jr)
    
    # choose 3 numbers randomly from 0 to 31
    rdNum = random.randint(0, 31)
    rsNum = random.randint(0, 31)
    rtNum = random.randint(0, 31)

    #corresponding registers
    rd = registers[rdNum]
    rs = registers[rsNum]
    rt = registers[rtNum]

    print("rd register: ", rd)
    print("rs register: ", rs)
    print("rt register: ", rt)

    print("Mips instruction: ", mnemonic, rd, rs, rt)

    #padding routine 
    rdNum = binPadding(bin(rdNum), 5)
    rsNum = binPadding(bin(rsNum), 5)
    rtNum = binPadding(bin(rtNum), 5)
    funct = binPadding(bin(funct), 6)


    binMachineCode = "000000" + rdNum + rsNum + rtNum + "00000" + funct
    print("Corresponding Binary: ", binMachineCode)
    hexNum = hex(int(binMachineCode, base=2))
    hex_str = hexNum[2:]
    hex_str = "0x0" + hex_str
    print("Corresponding machine code", hex_str)



machToMips()
#divAlg(4, 4)
#multAlg(4, 4)
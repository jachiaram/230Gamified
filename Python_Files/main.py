import random

#this is where binary numbers are generated, n is the max length of numbers to be generated
def generateRandomBinary(n):
    
    #generate length of binary string (min length 4)
    p = random.randint(4, n)

    #byte strings?
    key1 = ""
 
    # Loop to find the string
    # of desired length
    for i in range(p):
         
        # randint function to generate
        # 0, 1 randomly and converting 
        # the result into str
        temp = str(random.randint(0, 1))
 
        key1 += temp
         
    return(key1)

def multAlg(n, m):

    #can add another random number generation for length of strings for more variation
    binarySum = lambda a,b : bin(int(a, 2) + int(b, 2))
    multd = generateRandomBinary(n)
    multr = generateRandomBinary(m)
    prod = ""
    #length of resulting product string
    prodLen = n + m;

    #populate prod with zeros
    for i in range(prodLen):
        prod += "0"

    
    
    print("Use the multiplication algorithm to multiply " + multd + " and " + multr)

    print("Initial Values: ")
    print(multd)
    print(multr)
    print(prod)

    size = m
    for i in range(m):
        #if ending bit is 1 add to product
        if multr[size - 1] == '1':
            prod = binarySum(prod, multd)

        #shift multd left
        multd = "0" + multd

        #shift multr right        
        multr=list(multr)
        multr.pop()
        multr="".join(multr)
        size = size - 1
        
        #print out current values
        print("The current multiplicand: " + multd)
        print("The current multiplier: " + multr)
        print("The current product: " + prod)
    
    return

    

multAlg(4, 4)
from utils import binary_utils
from utils import quiz_prompter as prompt
import random
import math

#this makes more sense as a global variable up here
registers = [
        "$zero",
        "$at",
        "$v0",
        "$v1",
        "$a0",
        "$a1",
        "$a2",
        "$a3",
        "$t0",
        "$t1",
        "$t2",
        "$t3",
        "$t4",
        "$t5",
        "$t6",
        "$t7",
        "$s0",
        "$s1",
        "$s2",
        "$s3",
        "$s4",
        "$s5",
        "$s6",
        "$s7",
        "$t8",
        "$t9",
        "$k0",
        "$k1",
        "$gp",
        "$sp",
        "$fp",
        "$ra",
    ]

#r-type conversions
def rTypeToHex():
    rTypeInstructions = {
        0x20: "add",
        0x21: "addu",
        0x24: "and",
        0x08: "jr",
        0x27: "nor",
        0x25: "or",
        0x2A: "slt",
        0x2B: "sltu",
        0x00: "sll",
        0x02: "srl",
        0x22: "sub",
        0x23: "subu",
    }

    # Randomly choose registers from the register dict, different flows for different instructions
    funct, mnemonic = random.choice(list(rTypeInstructions.items()))
    shamt = 00000
    hex_str = ""
    instruct_str = ""
    
    if mnemonic != "jr":
        if mnemonic == "sll" or mnemonic == "srl":
            # choose 3 numbers randomly from 0 to 31
            rsNum = 0
            rdNum = random.randint(0, 31)
            rtNum = random.randint(0, 31)
            shamt = random.randint(0, 31)
            
            # corresponding registers and shamt value
            rd = registers[rdNum]
            rs = 0
            rt = registers[rtNum]

            instruct_str =  mnemonic + " " + rd + ", " + rt + ", " + str(shamt)
        else:
            #checks for slt down here?
            if mnemonic == "slt" or mnemonic == "sltu":
                rdNum = 1
            else:    
                # choose 3 numbers randomly from 0 to 31
                rdNum = random.randint(0, 31)
                
            rsNum = random.randint(0, 31)
            rtNum = random.randint(0, 31)
            
            # corresponding registers
            rd = registers[rdNum]
            rs = registers[rsNum]
            rt = registers[rtNum]
            
            instruct_str = mnemonic + " " + rd + ", " + rs + ", " + rt
        
        # padding routine
        rdNum = binary_utils.binPadding(bin(rdNum), 5)
        rsNum = binary_utils.binPadding(bin(rsNum), 5)
        rtNum = binary_utils.binPadding(bin(rtNum), 5)
        shamt = binary_utils.binPadding(bin(shamt), 5)
        funct = binary_utils.binPadding(bin(funct), 6)

        binMachineCode = "000000" + rsNum + rtNum + rdNum + shamt + funct
        hexNum = hex(int(binMachineCode, base=2))  # hex conversion, but removes leading 0s
        hex_str = hexNum[2:]

        # add back leading 0s
        while True:
            if len(hex_str) < 8:
                hex_str = "0" + hex_str
            else:
                hex_str = "0x" + hex_str
                hex_str = hex_str.lower()
                break
    else:
        instruct_str = "jr $ra"
        hex_str = "0x03e00008" 

    return instruct_str, hex_str

#j-type conversions
def jTypeToHex():
    jTypeInstructions = {0x2: "j", 0x3: "jal"}
    hex_str = ""
    instruct_str = ""

    opcode, mnemonic = random.choice(list(jTypeInstructions.items()))
   
    #So for the possible addresses we have 67,108,863 combinations with 26 bits
    #But we are dividing by 4 so our random number is from 0 to 268435452
    addr = random.randint(0, 268435452)
    instruct_str = mnemonic + " " +  hex(addr)
    addr = math.trunc(addr / 4)
    
    addrNum = binary_utils.binPadding(bin(addr), 26)
    opNum = binary_utils.binPadding(bin(opcode), 6)
    binNum = opNum + addrNum
    hexNum = hex(int(binNum, base=2))
    hex_str = hexNum[2:]

    # add back leading 0s
    while True:
        if len(hex_str) < 8:
            hex_str = "0" + hex_str
        else:
            hex_str = "0x" + hex_str
            hex_str = hex_str.lower()
            break
    
    return instruct_str, hex_str

#i-type conversions
def iTypeToHex():
    iTypeInstructions = {
        0x08: "addi",
        0x09: "addiu",
        0x0C: "andi",
        0x04: "beq",
        0x05: "bne",
        0x24: "lbu",
        0x25: "lhu",
        0x30: "ll",
        0x0F: "lui",
        0x23: "lw",
        0x0D: "ori",
        0x0A: "slti",
        0x0B: "sltiu",
        0x28: "sb",
        0x38: "sc",
        0x29: "sh",
        0x2B: "sw",
    }

    instruct_str = ""
    hex_str = ""

    opcode, mnemonic = random.choice(list(iTypeInstructions.items()))

    rsNum = random.randint(0, 31)
    rtNum = random.randint(0, 31)

    rs = registers[rsNum]
    rt = registers[rtNum]

    imm = random.randint(-40, 40)

    #conditionals based on diff instruct types:
    #arithmetic (addi, addiu, andi, ori)
    if mnemonic == "addi" or mnemonic == "addiu" or mnemonic == "andi" or mnemonic == "ori" or mnemonic == "beq" or mnemonic == "bne":
        
        instruct_str = mnemonic + " " + rs + ", " + rt + ", " + str(imm)
    
    elif mnemonic == "slti" or mnemonic == "sltiu": #set on instruct (slti, sltiu)
        rsNum = 1
        rs = registers[rsNum]
        instruct_str = mnemonic + " " + rs + ", " + rt + ", " + str(imm)
    
    elif mnemonic == "lui":
        rsNum = 0
        instruct_str = mnemonic + " " + rt + ", " + str(imm)
    
    else:   #storing and loading from memory (lbu, lhu, ll, lw, sb, sc, sh, sw)
        imm = random.randint(0, 16)
        instruct_str = mnemonic + " " + registers[rtNum] + ", " + str(imm) + "(" + registers[rsNum] + ")"
            
    opcode = binary_utils.binPadding(bin(opcode), 6)
    rsNum = binary_utils.binPadding(bin(rsNum), 5)
    rtNum = binary_utils.binPadding(bin(rtNum), 5)
    imm = binary_utils.binPadding(bin(imm), 16)

    binNum = opcode + rsNum + rtNum + imm
    hexNum = hex(int(binNum, base=2))

    hex_str = hexNum[2:]

    # add back leading 0s
    while True:
        if len(hex_str) < 8:
            hex_str = "0" + hex_str
        else:
            hex_str = "0x" + hex_str
            hex_str = hex_str.lower()
            break

    return instruct_str, hex_str
    

# basic machine to mips game
def machToMips():
    #these are the mips and hex parts of the generated instructions, this can be modified for more games (MIPS -> machine and vice versa)
    #passing in a bool var to determine which to show could work for now
    instruct_str = ""
    hex_str = ""

    # First choose R,I, or J at random
    selected = random.randint(0, 2)
    
    # split into 3 branches
    if selected == 0:
        instruct_str, hex_str = rTypeToHex()
    elif selected == 1:
        instruct_str, hex_str = jTypeToHex()
    else:
        instruct_str, hex_str = iTypeToHex()

    print("Convert the MIPS instruction: ", instruct_str)

    # No counter here, since answerLoop counter takes care of it, 3 attempts
    #if bool == True:
    #else:
    if prompt.answerLoop("Hex Conversion", hex_str):
        return True
    else:
        return False


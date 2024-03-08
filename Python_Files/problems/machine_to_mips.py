from utils import binary_utils
from utils import quiz_prompter as prompt
import random


#r-type conversions
def rTypeToHex(registers):
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
        # TODO: Handle special cases (sll, srl, slt, jr)
        if mnemonic == "sll" or mnemonic == "srl":
            # choose 3 numbers randomly from 0 to 31
            rsNum = 0
            rdNum = random.randint(0, 31)
            rtNum = random.randint(0, 31)
            shamt = random.randint(0, 31)
            
            # corresponding registers and shamt value
            rd = registers[rdNum]
            rs = 0;
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


# basic machine to mips game
def machToMips():
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

    # TODO: Need to fix this
    # First choose R,I, or J at random
    # types = ["R", "I", "J"]
    # selected = random.randint(0, 3)
    # print("Selected instruction type: ", types[selected])
    # split into 3 branches

    # Randomly choose the opcode/ funct code from list (should have opcode, type, and mnemonic at this point)
    
    iTypeInstructions = {
        0x8: "addi",
        0x9: "addiu",
        0xC: "andi",
        0x4: "beq",
        0x5: "bne",
        0x24: "lbu",
        0x25: "lhu",
        0x30: "ll",
        0xF: "lui",
        0x23: "lw",
        0xD: "ori",
        0xA: "slti",
        0xB: "sltiu",
        0x28: "sb",
        0x38: "sc",
        0x29: "sh",
        0x2B: "sw",
    }
    jTypeInstructions = {0x2: "j", 0x3: "jal"}

    instruct_str, hex_str = rTypeToHex(registers)

    print("Convert the MIPS instruction: ", instruct_str)

    # No counter here, since answerLoop counter takes care of it, 3 attempts
    if prompt.answerLoop("Hex Conversion", hex_str):
        return True
    else:
        return False

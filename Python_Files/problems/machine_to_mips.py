from utils import binary_utils
import random


class MipsInstruct:
    functType = ""
    opcode = ""
    mnemonic = ""
    # this should always follow this order rd, rs, rt
    registers = ["", "", ""]
    shamt = ""
    funct = ""
    imm = ""


# basic machine to mips game
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

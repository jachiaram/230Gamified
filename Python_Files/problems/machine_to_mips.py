from utils import binary_utils


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
    # define dictionaries for different parts of mip instructions to be translated
    # dictionary instrType = list out all possible for core instr set
    # i.e.
    # dictionary registers = pair all registers to corresponding number
    # dictionary mnemonics = this should be fed into from instr type dict

    # define a function that will be able to choose a random value in a dictionary
    # choose random value for

    return

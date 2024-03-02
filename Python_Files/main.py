import os
import problems.multiply_algorithm as multiply_algorithm
import problems.division_algorithm as division_algorithm


def clearTerminalWindow():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def mainMenuLoop():
    # clear_screen()
    title = """
     ______   ______    _____     _______                _     ___  _             _ 
    (_____ \\ (_____ \\  (_____)   (_______)              (_)   / __)(_)           | |
      ____) ) _____) ) _  __ _    _   ___  _____  ____   _  _| |__  _  _____   __| |
     / ____/ (_____ ( | |/ /| |  | | (_  |(____ ||    \\ | |(_   __)| || ___ | / _  |
    | (_____  _____) )|   /_| |  | |___) |/ ___ || | | || |  | |   | || ____|( (_| |
    |_______)(______/  \\_____/    \\_____/ \\_____||_|_|_||_|  |_|   |_||_____) \\____|
                                                                                    
    """

    userInput = "c"
    while not userInput == "q":

        print(title)
        print("<1> Multiply")
        print("<2> Divide")
        print("\n<q> Quit")
        userInput = input("enter choice:")

        if userInput == '1':
            multiply_algorithm.multAlg(4, 4)
        elif userInput == '2':
            division_algorithm.divAlg(4, 4)
        else:
            clearTerminalWindow()
            continue
            

# divAlg(4, 4)
# multAlg(4, 4)
                










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


# divAlg(4, 4)
# multAlg(4, 4)

mainMenuLoop()

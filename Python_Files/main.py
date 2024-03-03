import os
# import problems.multiply_algorithm as multiply_algorithm
# import problems.division_algorithm as division_algorithm
import utils.quiz_prompter as quiz
import problems.machine_to_mips as machine_to_mips


# Determines whether system is unix or windows based,
# then sets appropriate clear for terminal
def clearTerminalWindow():
    if os.name == "nt":  # Windows based
        _ = os.system("cls")
    else:  # Unix based
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

    userInput = ""
    while not userInput == "q":

        print(title)
        print("<1> Multiply 4-bit")
        print("<2> Divide 4-bit")
        print("<3> Mips To Machine Code 1-line")
        print("\n<q> Quit")
        userInput = input("enter choice:")

        if userInput == '1':
            # multiply_algorithm.multAlg(4, 4)
            quiz.gameLoop(1)
        elif userInput == '2':
            # division_algorithm.divAlg(4, 4)
            quiz.gameLoop(2)
        elif userInput == '3':
            machine_to_mips.machToMips()
        else:
            clearTerminalWindow()
            continue


mainMenuLoop()


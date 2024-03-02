import os
import problems.multiply_algorithm as multiply_algorithm
import problems.division_algorithm as division_algorithm


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

    userInput = "c"
    while not userInput == "q":

        print(title)
        print("<1> Multiply 4-bit")
        print("<2> Divide 4-bit")
        print("\n<q> Quit")
        userInput = input("enter choice:")

        if userInput == '1':
            multiply_algorithm.multAlg(4, 4)
        elif userInput == '2':
            division_algorithm.divAlg(4, 4)
        else:
            clearTerminalWindow()
            continue


mainMenuLoop()

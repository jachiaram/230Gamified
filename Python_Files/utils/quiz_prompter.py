# Houses the interaction logic for the interactive
# quizzing portion of the application
from problems import multiply_algorithm as mprob
from problems import division_algorithm as dprob
from problems import machine_to_mips as machineprob


# Determines question based on problemType, then handles accordingly
def questionGenerator(problemType):
    if problemType == 1:
        return mprob.multAlg(4, 4)
    if problemType == 2:
        return dprob.divAlg(4, 4)
    if problemType == 3:
        return machineprob.machToMips()


def writeState(current_question):
    # TODO print state of game
    print("This is where my current state would go. IF I HAD ONE")
    # cout question


def gameLoop(problemType):
    if questionGenerator(problemType):
        print("\n\nYOU WIN!!!!!!!!!!!!!!!!!\n")
    else:
        print("\n\nYou failed me.......\n")
    return


# user goes here when they get an answer wrong.
# re-prompts user until answer is correct
def answerLoop(expectedValueType, expectedValue):

    givenVal = input(expectedValueType + ": ")
    if givenVal == expectedValue:
        print("correct!")
        return True

    maxPartAttempts = 3
    partAttempts = 1
    # Loop until answer is correct or attempts = 3
    while True:
        if partAttempts >= maxPartAttempts:
            print("Max attempts exceeded!\n" + "The correct "
                  + expectedValueType + " was " + expectedValue)
            return False

        print("That answer was incorrect" + "\n"
              + "Try again! OR <q> to quit OR <g> to give up")
        givenVal = input(expectedValueType + ": ")

        if givenVal == 'q':  # quit
            print("\n-------------------\nThanks for Playing!")
            exit()
        if givenVal == 'g':  # give up
            print("The correct " + expectedValueType + " was " + expectedValue)
            return False
        if givenVal == expectedValue:  # correct answer
            print("correct!")
            return True
        else:
            partAttempts += 1  # increment attempts

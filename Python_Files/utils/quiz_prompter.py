# Houses the interaction logic for the interactive quizzing portion of the application
def writeQuestion():
    # call questionGenerator()
    print("enter " + current_question_part + ":")
    # cout question
    
def gameLoop():
    # TODO game loop logic
    
    # user comes here after selecting a game to play
    # call writeQuestion()
    # prompt for answer

    # if wrong, 
        #call reviseLoop
    # else
    # loop
    return
    
# user goes here when they get an answer wrong. re-prompts user until answer is correct
def reviseLoop(givenValue, expectedValue, expectedValueType):
    
    correct = False

    # while incorrect, loop grab new input until correct
    while not correct:
        print("That answer was incorrect" + "\n" + "Try again! OR <q> to quit")
        givenVal = input("New " + expectedValueType + ":")

        if givenVal == 'q':
            print("\n-------------------\nThanks for Playing!")
            exit()
        else:
            print(givenVal)
            correct = True

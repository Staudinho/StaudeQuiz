from random import randint
import getQuestion as getQ
class handleQuestionFlows:

    def __init__(self):
        pass

    def handleQuestionFlow(self):
        # random value for the question to be selected
        value = randint(1, 30)

        # select question from pool, first create object, then call it
        quest = getQ.getQuestions(value)
        data = quest.choseQuestion()

        # UI part: show questions and possible answers
        print (data[0])
        print ('1: ', data[1])
        print ('2: ', data[2])
        print ('3: ', data[3])
        print ('4: ', data[4])

        # get users choice
        userinput = input ("Please enter the correct answer: ")
        correct = data[5]

        # evaluate the users entry, is it correct or not?
        if userinput == correct:
            print ("richtig")
            answer = True
        else:
            print ('falsch! ', correct)
            answer = False
        print()

        return answer

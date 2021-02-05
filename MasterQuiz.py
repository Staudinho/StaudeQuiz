import handleQuestionFlows as handleQs
import time

print ()
print ()
print ("**************************************")
print ("WELCOME to MASTER QUIZ")
print ('**************************************')
print ()
print ()

#initialize question constructor and timer
hQs = handleQs.handleQuestionFlows()
correctanswers = 0
starttime = time.perf_counter()

#start with questions
for i in range (1,11):
    print ("question number: "+str(i))
    answer = hQs.handleQuestionFlow()
    if answer==True:
        correctanswers += 1
    # measure end time        
    endtime = time.perf_counter()
    duration = round(endtime - starttime)
    print ("Aktuelle Zeit "+str(duration)+" Sekunden")

# calculate points
points = (60-duration)*correctanswers

print ()
print ()
print ('Spiel beendet')
print ()
print ('Richtige Antworten: '+str(correctanswers))
print ('benötigte Zeit: '+str(duration)+' Sekunden')
print ()
print ()
print ('PUNKTE: '+str(points))


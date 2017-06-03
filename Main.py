#The imports that we need.
from guizero import App, Text, PushButton

#The main app window
app = App(title="Scoreboard")

#The scores
aScore = 0
bScore = 0
#Change these strings to whatever you like!
aName = "TeamA"
bName = "TeamB"

#Increase team A's score
def upA():
    global aScore
    aScore = aScore + 1
    showScore()

#Increase team B's score
def upB():
    global bScore
    bScore = bScore + 1
    showScore()

#Decrease team A's score
def downA():
    global aScore
    aScore = aScore - 1
    showScore()

#Decrease team B's score
def downB():
    global bScore
    bScore = bScore - 1
    showScore()

#Resets everything to 0
def reset():
    global aScore
    global bScore

    aScore = 0
    bScore = 0
    
    showScore()

#Setup all the buttons and labels
topMessage = Text(app, text="{}".format(aName) + " vs " + "{}".format(bName), size=40)
scoreMessage = Text(app, text="0 vs 0", size=40)
aUpButton = PushButton(app, command=upA, text="+" + "{}".format(aName) + "+")
bUpButton = PushButton(app, command=upB, text="+" + "{}".format(bName) + "+")
aDownButton = PushButton(app, command=downA, text="-" + "{}".format(aName) + "-")
bDownButton = PushButton(app, command=downB, text="-" + "{}".format(bName) + "-")
resetButton = PushButton(app, command=reset, text="Reset")

#Updates the score on the screen
def showScore():
    global aScore
    global bScore

    scoreMessage.set("{:d}".format(aScore) + " vs " + "{:d}".format(bScore))

#Displays the app window on the screen.
app.display()

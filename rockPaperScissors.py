player1 = input("Player 1 enter your name: ")
player2 = input("Player 2 enter your name: ")
winner = ""

p1score = 0
p2score = 0

input1 = ""
input2 = ""
validInputs = ['rock', 'scissors', 'paper', 'lizard', 'spock', 'i quit!']
duplicateCheck =" "

#module that updates the score and returns true or false depending if player 1 won or not
def getScore(input1, input2):
    global p1score
    global p2score
    if input1 == "rock":
        if (input2 == "scissors" or input2 == "lizard"):
            p1score+=1
            return True
        else:
            p2score+=1
            return False
    elif input1 == "scissors":
        if (input2 == "paper" or input2 == "lizard"):
            p1score+=1
            return True
        else:
            p2score+=1
            return False
    elif input1 == "spock":
        if (input2 == "rock" or input2 == "scissors"):
            p1score+=1
            return True
        else:
            p2score+=1
            return False
    elif input1 == "lizard":
        if (input2 == "spock" or input2 == "paper"):
            p1score+=1
            return True
        else:
            p2score+=1
            return False
    elif input1 == "paper":
        if (input2 == "rock" or input2 == "spock"):
            p1score+=1
            return True
        else:
            p2score+=1
            return False
    
#module to get verb depending on the inputs
def getVerb(input1, input2):
    
    if input1 == "rock":
        if (input2 == "scissors") :
            return "crushes"
        elif (input2 == "lizard") :
            return "crushes"
    if input1 == "scissors":
        if (input2 == "paper") :
            return "cuts"
        elif (input2 == "lizard") :
            return "decapitates"
    if input1 == "spock":
        if (input2 == "rock") :
            return "vaporises"
        elif (input2 == "scissors") :
            return "smashes"
    if input1 == "lizard":
        if (input2 == "spock") :
            return "posions"
        elif (input2 == "paper") :
            return "eats"
    if input1 == "paper":
        if (input2 == "rock") :
            return "covers"
        elif (input2 == "spock") :
            return "disproves"
#module to verify and get the input from the user
def getInput(player):
    temp = True
    global player2
    global duplicateCheck
    while temp:
        userinput = (input(player + " pick one of rock, scissors, paper, lizard, spock: ")).lower()
        
        if userinput in validInputs:
            if (player2 == player):
                if userinput == duplicateCheck :
                    print("Invalid choice, try again:")
                    continue
                else:
                    duplicateCheck =" "
                    return userinput
            temp = False
            duplicateCheck = userinput
            return userinput

        else:
            print("Invalid choice, try again:")

while (input1 != "i quit!" and input2 != "i quit!"):
   
    input1 = getInput(player1) #verify the input 
    if (input1 == "i quit!"):  
        break
    input2 = getInput(player2)
    if (input2 == "i quit!"):
        break
    if (getScore(input1, input2)): #if player one wins
        verb = getVerb(input1,input2) 
        if (verb == None): # if verb is not found, switch th inputs
            verb = getVerb(input2, input1)
        print(input1 ,verb, input2, player1, " wins! Total: ", player1, " ",p1score, player2, " ",p2score)
    else:
        verb = getVerb(input1,input2)
        if (verb == None): # if verb is not found, switch th inputs
            verb = getVerb(input2, input1)
        print(input2 , verb, input1, player2, " wins! Total: ", player1, " ",p1score, player2, " ",p2score)


if (p1score > p2score):
    winner = player1
elif (p2score < p1score):
    winner = player2
else:
    winner = "none"
print("The final socre is ", player1, " ", p1score, player2, " ",p2score,". " ,winner, " wins!")
    




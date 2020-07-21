#  Raja mantri chor sipahi game
#  Python 3
#This is a multiplayer games which first asks for the players name and then assign randomly assign any role.
#Now the Mantri who is you or any other person sitting next to you have to type the correct name.
#Since I doesn't have much knowledge of server processing, this game is not entirely multiplayer.
#Either he four people have to be together or only one person can play this by just typing any four names.
#This is like a very begginers version. 
#I may improve it over time and maybe in future you can play this in your phone with friends. 
#Ciao



#Import the random libary to randomly assign roles and time libary to use the function sleep
#The program can run without the time and sleep(). I used it for little suspence, thrill and just to slow it a little bit.
import random
import time


#Trying hard to make the game look cool       
def welcome():
    print('##############################################################')
    time.sleep(1)
    print('#                  Raja Mantri Chor Sipahi                   #')
    time.sleep(1)
    print('##############################################################')


#Randomizing the roles
def picking():
    picking=["Raja", "Mantri","Chor","Sipahi"]
    picked=random.sample(picking,4)
    return picked

#Asking for players name
def playerInput():
    player=[]
    print("Enter player name one by one")
    for i in range(0,4):
        player.append(input("Enter name: "))

    #if players is less than 4 or no name is given then Sorry bro you can't play
    if len(player)<4 or '' in player:
        print("Less player")
    else:
        return player



#Real headace starts here

def assignment(players,points):
    assign=dict()
    i=0
    picked=picking()

    #We create a dictionary where Players and points together creates a list which are the values to the key of the role name
    for item in picked:
        assign[item]=[players[i],points[i]]
        i+=1
    print("Shuffling...")
    time.sleep(0.5)                 
    #print(assign)
    print("Done")
    time.sleep(0.5)
    print('##############################################################')
    return assign


#Keeping track of the scores and prining them
def scoress(assign):
    scores=list(assign.values())
    scores
    #print("score list",scores)
    print("Scores are:")
    time.sleep(0.5)
    updatedPoints=[]
    print('##############################################################')
    for score in scores:
        print(str(score[0])+": "+str(score[1]))
        updatedPoints.append(score[1])
    #print("in scoress updated points",updatedPoints)
    print('##############################################################')
    return updatedPoints


#Main game function
def game(players,points):
    assign=assignment(players,points)
    #print(type(assign))
    #print(assign)
    time.sleep(0.1)
    print(assign["Raja"][0], ":- Mera Mantri Kon")
    print(assign["Mantri"][0], ":- Mein Maharaj")
    time.sleep(0.2)
    print(assign["Raja"][0], ":- Chor Siphai ka pata lagao")

    assign["Raja"][1]+=1000
    assign["Sipahi"][1]+=300

    #loop will run till you press or type anything other than typing "restart" and pressing enter key
    while True:
        guess=input("Enter your guess who is chor: ")
        if(guess.lower()==assign["Chor"][0].lower()):
            time.sleep(0.5)
            print("Your guess is correct.")
            assign["Chor"][1]+=0
            assign["Mantri"][1]+=800
            break
        elif guess.lower()==assign["Sipahi"][0].lower():
            time.sleep(0.5)
            print("Your guess is wrong")
            time.sleep(0.5)
            print("              Chor is",assign["Chor"][0])
            assign["Chor"][1]+=800
            assign["Mantri"][1]+=0
            break
        else:
            print("Invalid Input")
        
    
    return scoress(assign)
    #print(scores)
    
#To execute all other above functions
def main():
    welcome()
    time.sleep(1)
    players=playerInput()
    initialPoints=[0,0,0,0]
    while True:

        #upPoints is same as updatedpoints. But the updatedpoints will be returned by the game function.
        #So I changed the name so I don't get confuse myself in future.
        upPoints=game(players,initialPoints)
        turn=input("Press enter for next turn or type restart to restart the game or any other key to exit ")
        if turn=="":
            initialPoints=upPoints
            #print("In main initial points after uppoints",initialPoints)
            continue
        elif turn.lower()=="restart":
            players=playerInput()
            initialPoints=[0,0,0,0]
        else: break

#Finally we can now play. Run this Now.
main()
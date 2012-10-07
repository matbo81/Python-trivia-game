##### THIS IS THE GAME


##### QUESTION ZONE:

    ##### here are all variables of the questions. 
    ##### if you add more or delete some, just update the list "questions" and the ANSWER ZONE !!

question1 = ("What\'s 12+6? ")
question2 = ("What\'s the name of the USA president? ")
question3 = ("What\'s the height of the Eiffel tower? ")
question4 = ("In which year the Impossible Project team produced the first film for sale? ")
question5 = ("How many people lives in Amsterdam? ")
question6 = ("In what red-blooded body organ are the vitamins A, D, E and K stored? ")
question7 = ("Who is the author behind the vampire book series Twilight? ")
question8 = ("Who is the author behind the Harry Potter books? ")

    ##### this is the list   questions

questions = [question1, question2, question3, question4, question5, question6, question7, question8]

##### ANSWER ZONE: if you make changes in the question zone, don't forget to syncronise this zone (the variable and the list)!!!! 

    ##### here are all variables of the answers. 

answer1 = ("18")
answer2 = ("Barack Obama")
answer3 = ("324")
answer4 = ("2010")
answer5 = ("820000")
answer6 = ("liver")
answer7 = ("Stephenie Meyer")
answer8 = ("J.K. Rowling")

    ##### this is the list   answers

answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8]

##### POINTS ZONE

points = 0

##### GAME INTRO ZONE

    ##### player puts his name as long as he thinks is correct and confirm it with Yes

correct = False
while correct == False:
    name = input("What's your name? ")
    print("Your name is", name)
    ok = input("Is that correct? ")
    if ok == "Yes" or ok == "yes" or ok == "YES":
        print("Good, let's go on!\n")
        correct = True
    else:
        print("Mh? Try again and confirm with Yes!")

##### GAME PLAY ZONE
##### 1 "function" and 1 "for"-loop for all questions!

    ##### This is the quest-function
        
def quest(x):
    '''
    this function asks the player question X, checks if player's answer is right and eventually changes the variable points.
    no examples needed
    '''
    
    global points
    answerPlayer = input(questions[x])
    if answerPlayer == answers[x]:
        print("Well done,", name + ", 10 points gained! Let's move to the next question.\n")
        points +=10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[x], ". Next question...\n")


    ##### This is the counter who tells the quest-function how many and which questions it must asks the player
        
for x in range(len(questions)):
    print("At the moment your total points are", points)
    print("Challenge", x+1, "\n")
    quest(x)

##### END ZONE
    
print("\nYou finished the game with a total of", points, "points! Thanks for playing!")



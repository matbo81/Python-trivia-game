question1 = ("What\'s 12+6? ")
question2 = ("What\'s the name of the USA president? ")
question3 = ("What\'s the height of the Eiffel tower? ")
question4 = ("In which year the Impossible Project team produced the first film for sale? ")
question5 = ("How many people lives in Amsterdam? ")
question6 = ("In what red-blooded body organ are the vitamins A, D, E and K stored? ")
question7 = ("Who is the author behind the vampire book series Twilight? ")
question8 = ("Who is the author behind the Harry Potter books? ")
points = 0
name = input("What\'s your name? ")
print("Your name is", name)
ok = input("Is that correct? ")

if ok == "Yes":
    print("Good, let\'s go on!")
elif ok =="yes":
    print("Good, let\'s go on!")


answer1 = input(question1)
if answer1 == "18":
    print("Well done,", name , "10 points gained!, let\'s move to the next question.")
    points = 10
else:
        print("Wrong! 0 points gained, the correct answer was: 18. Next question...")
        

answer2 = input(question2)
if answer2 == "Barack Obama":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else:
        print("Wrong! 0 points gained, the correct answer was: Barack Obama. Next question...")

answer3 = input(question3)
if answer3 == "324":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else:
        print("Wrong! 0 points gained, the correct answer was: 324. Next question...")

answer4 = input(question4)
if answer4 == "2010":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else:
        print("Wrong! 0 points gained, the correct answer was: 2010. Next question...")

answer5 = input(question5)
if answer5 == "820000":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else:
        print("Wrong! 0 points gained, the correct answer was: 820000. Next question...")

answer6 = input(question6)
if answer6 == "liver":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else:
        print("Wrong! 0 points gained, the correct answer was: liver. Next question...")

answer7 = input(question7)
if answer7 == "Stephenie Meyer":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else: 
        print("Wrong! 0 points gained, the correct answer was: Stephenie Meyer. Next question...")

answer8 = input(question8)
if answer8 == "J.K. Rowling":
    points = points + 10
    print("Well done,", name , "10 points gained!, you have", points, "points!", "Next question...")
    
else: 
        print("Wrong! 0 points gained, the correct answer was: J.K. Rowling. Next question...")



print("You finished the game with a total of", points, "points! Thanks for playing!")
        


        
    


#!/urs/bin/env python3
#simple math game
#exercise for random module
import random

count = 2
score = 0
CorrectAnswers = {}
userAnswers	 = {}

gameLife = 3
while(gameLife >= 0):
        try:
                def game_Questions():
                        randQuestion_One = random.randint(10,20)
                        randQuestion_Two = random.randint(1,10)
                        randQuestion = random.randint(0,1)
                        list 	= [randQuestion_One + randQuestion_Two, randQuestion_One - randQuestion_Two]
                        answer 	= list[randQuestion]
                        
                        if(randQuestion == 0):
                                print(randQuestion_One, " + ", randQuestion_Two, "= ?\b")
                        else:
                                print(randQuestion_One, " - ", randQuestion_Two, "= ?\b")	
                                
                        return answer

                Question_Answers = game_Questions()
                userAnswer = int(input(""))
                
                
                if(userAnswer != Question_Answers):
                        gameLife  -=1
                        
                        if(gameLife == 0):	
                                print("Wrong Answer\n","-"*60, "\nGame Over")
                        else:
                                print("\nWrong Answer\n")
                                
                elif(userAnswer is Question_Answers):
                        print("\nCorrect Answer! \n")
                        score += 1
                else:
                        print("Wrong Input Dectected")
                        
                for Record in range(count -1, count):
                        CorrectAnswers.update({"Answer in Number "+str(Record)+":" : Question_Answers}) 
                        userAnswers.update({"You Answered Number "+str(Record)+":" : userAnswer})
                        
                count += 1
        except Exception :
                print("Invalid Input, Input an Integer not a Character")

                
print("score: ",score)
print(sorted(CorrectAnswers.items()))
print(sorted(userAnswers.items()))

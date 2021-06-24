name=input('This is a quiz based on your knowledge of cars. Your name is : ')
print('Hi,',name)
score=0
lives=3
x=0
#Question 1
answer_1=input('1. Which is the fastest Ferarri built in the world ? \n a) Ferarri SF90 \n b) Ferarri 812 Superfast \n c) Ferarri Roma \n d) Ferarri Italia \nYour answer is : ')
if answer_1=='Ferarri SF90' or answer_1.lower()=='a':
    print('Correct! \nRemaining lives =',lives,)
    print('\n')
    score=score+1
else:
    print('Incorrect! The correct answer is Ferarri SF90 \nRemaining lives =',lives-1,)
    print('\n')
    lives=lives-1

#Question 2
answer_2=input('2. Which is the SUV that is produced by lamborghini ? \n a) Huracan \n b) Aventador \n c) Urus \n d) Evo \nYour answer is : ')
if answer_2=='Urus' or answer_2.lower()=='c':
    print('Correct! \nRemaining lives =',lives,)
    print('\n')
    score=score+1
else:
    print('Incorrect! The correct answer is Lamborghini Urus \nRemaining lives =',lives-1,)
    print('\n')
    lives=lives-1

#Quetion 3
answer_3=input('3. Which is the most expensive car in the world ? \n a) Rolls Royce Sweptail \n b) Bugatti La Voiture Noire \n c) Bugatti Chiron \n d) Mercedes Maybach \nYour answer is : ')
if answer_3=='Bugatti La Voiture Noire' or answer_3.lower()=='b':
    print('Correct! \nRemaining lives =',lives,)
    print('\n')
    score=score+1
else:
    print('Incorrect! The correct answer is Bugatti La Voiture Noire \nRemaining lives =',lives-1,)
    print('\n')
    lives=lives-1

#Question 4
answer_4=input("4. Which is the Porsche's only electric car ? \n a) Panamera \n b) 911 \n c) Cayenne \n d) Taycan \nYour answer is : ")
if answer_4=='Taycan' or answer_4.lower()=='d':
    print('Correct! \nRemaining lives =',lives,)
    print('\n')
    score=score+1
else:
    print('Incorrect! The correct answer is Porsche Taycan \nRemaining lives =',lives-1)
    print('\n')
    lives=lives-1

#Question 5
answer_5=input('5. Which is not a model of Jaguar ? \n a)I-Pace \n b) E-Pace \n c) X-Pace \n d) F-Pace \nYour answer is : ')
if answer_5=='X-Pace' or answer_5.lower()=='c':
    print('Correct! \nRemaining lives =',lives,)
    print('\n')
    score=score+1
else:
    print('Incorrect! The correct answer is X-Pace \nRemaining lives =',lives-1,)
    print('\n')
    lives=lives-1
if lives==0:
    print('You have run out of lives...... \nBetter Luck next time !')
    
#Total Score
print('Total Score =',score)

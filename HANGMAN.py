print('\t \t GUESSING GAME by syed')

import random
import time

def countdown(t):

    while t>0:
        print(t,end=' ')
        t = t-1
        time.sleep(1)
    print()


words = ['tiger','nehru','avengers','paris','dhoni']
clues = {'tiger':'WILD ANIMAL',
         'nehru':'One of the Prime Minister of India',
         'avengers':'Movie where superheros unite',
         'paris':'City lovers visit',
         'dhoni':'Well knwon cricketer'}

word = random.choice(words)
print('\nYour clue is :',clues[word])
time.sleep(3)
lives = 3
suggestion = []
for i in range(0,len(word)):
    suggestion.append('_')
    
countdown(3)

while '_' in suggestion:
    if lives >0:
        for i in suggestion:
            print(i,end=' ')
        print()
        x = input('\nEnter your guess: ')
        if len(x)<2:
            if x in word:
                if word.count(x) == 1:
                    print('\nRight Guess')
                    index =word.index(x)
                    suggestion.insert(index,x)
                    suggestion.pop(index+1)
                    word = word.replace(x,'*')

                elif word.count(x) == 2:
                    print('\nRight Guess')
                    index =word.index(x)
                    suggestion.insert(index,x)
                    suggestion.pop(index+1)
            
                    index =word.index(x,index+1,len(word))
                    suggestion.insert(index,x)
                    suggestion.pop(index+1)
                    word = word.replace(x,'*')
                


                

            else:
                print('\nWRONG GUESS')
                lives = lives -1
                time.sleep(2)
                print('Lives left= ',lives)

        else:
            print('\nINPUT ERROR')
    else:
        print('\nYou Lost!')
        break
else:
    print('\nYou won!')



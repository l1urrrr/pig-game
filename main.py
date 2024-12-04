import random
import  time
from itertools import count
#make variables to track how many players there are and how many rounds
# there will be
p = int(input('how many players ?'))
r = int(input('how many rounds?'))

#create a set of numbers to represent the dice :
dice = [1,2,3,4,5,6]
# use for loop to iterate through rounds
for round in range (0,r):
    print(f'round {round}!\n')
    class User :
       score = 0 #class attribute to make sure that each object has a
       # starting score of 1
    #then we have a nested for loop to iterate through the players in the game
    for player in range (0,p):
        User.score = 0
        User_turn  = random.choice(dice) #randomly selects an element from
        # dice list
        print(f'player number {player} : \n ') # just outlines which
        # player's go it is
        #then there's the conditional to check if a player rolled a one and
        # how their score will change
        if  User_turn !=  1 :
            User.score += 1 # when 1 isn't rolled increments score by one
            print(f'you rolled a {User_turn}! Better luck next time !Your '
                  f'score is {User.score}') #tells you what a player rolled
            # and what their score is
        else:
            print(f'you rolled a one your score is:{User.score}') #pretty
            # self-explanatory
        if  player != p-1:
            print('next Player!')
        if not r == 1:
            print ('Next round!!!')
        time.sleep(3)
    time.sleep(7)
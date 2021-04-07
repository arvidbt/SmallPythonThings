import random
import sys

print("Welcome to a game of DEATHROLL!!")
player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")
roll = int(input("Enter highest roll value: "))
bet = int(input("Please enter how much to gamble: "))
i = 0;
while(roll != 1):
    i = i % 2
    if(input("write \"roll\" to roll: ") == "roll"):
        roll = random.randint(1, roll)
        if(i == 0):
            print(player1 + " rolled " + str(roll))

        elif(i == 1):
            print(player2 + " rolled " + str(roll))
    i = i + 1

if i == 1:
    print(player2 + " wins " + str(bet*2))

else:
    print(player1 + " wins " + str(bet*2))
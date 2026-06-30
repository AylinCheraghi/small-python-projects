#Cows and Bulls is a code-breaking game that tests logical thinking and deduction skills. 
#In this game, the computer generates a secret 4-digit number with unique digits, and the
#player attempts to guess it. After each guess, the program provides hints in the form of
#bulls and cows, helping the player narrow down the correct number.

import random

def getDigits(num):
    return[int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li)  == len(set(num_li)):
       return True
    else:
       return False

def numOfBullsCows (num, guess):
    bull_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
     
    for i,j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] +=1
        return bull_cow
        

print("Enter of tries: ")
tries = int(input())

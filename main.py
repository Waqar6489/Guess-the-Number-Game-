'''If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number.'''

import random
n= random.randint(1,150)
Gusses=1
a=-1
while(a!=n):
    a=int(input("Gusses the Number : "))
    if(n<a): 
        print("lower the Number Please")
        Gusses +=1
    elif(n>a):
        print("Higher the number Please")
        Gusses+=1
print(f"Guess the number {n} of atempt {Gusses}")            

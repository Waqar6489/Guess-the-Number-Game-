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
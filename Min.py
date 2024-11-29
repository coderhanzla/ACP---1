
import random
num = random.randint(1,10)
print("The computer has chosen a number between 1-10.")

turns = 5

for i in range( 1 , 11):
  
  i = int(input("Enter the number: "))

  if (i==num):
    print("Congratulation you Guessed the number")

  elif i>num:
    print("Number is lesser")
    turns-=1

  elif i<num:
    print("Number is greater")
    turns-=1

  if turns ==0:
        print("You have lost.No.of turns=0")

  
  

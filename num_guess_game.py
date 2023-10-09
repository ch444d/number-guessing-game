import random

randomnum1 = random.randint(0,10000)

randomnum = int(randomnum1)

# print(randomnum)

number1 = input("Choose a number between 0 and 10000: ")

number = int(number1)

guesses = 1

# print(type(number))
# print(type(randomnum))


while (number != randomnum):
  
  if (number > randomnum):
    print("\nNeed to go lower.")
    number = int(input("Guess again: "))
    guesses += 1
    continue
  elif (number < randomnum):
    print("\nNeed to go higher. ")
    number = int(input("Guess again: "))
    guesses += 1
    continue

    
    
#  else:
#    print("YOU WIN!!!!!")
  elif (number == randomnum):
#    print("YOU WIN!!!!!! ")
    break

print("\nYou Win!")
print(f"It took you {guesses} guesses.")

# print(randomnum)
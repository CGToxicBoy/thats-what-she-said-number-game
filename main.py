import random

random_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")

while True:
  guess= input("Guess what i just picked: ")
  if int(guess) > random_number:
      print('Thats what she said, "Its too big"')
  elif int(guess) == random_number:
      print('Thats what she said, "Thats exactly what i wanted"')
      break
  else:
      print("Its too small")




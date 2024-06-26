# rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Code 👇
import random

# choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')
# counter = random.randint(0,2)

plays = [rock,paper,scissors]
again = True
while again:
  choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n')

  if not isinstance(choice, int) or choice > 2:
    print('Invalid input!')
    continue

  choice = int(choice)
  counter = random.randint(0,2)
  
  print(plays[choice], '\n')
  print('Computer chose: \n', plays[counter])

  if choice == counter:
    print('Tie!')
  elif choice == 0 and counter == 1: # player rock, comp paper
    print('You lose!')
  elif choice == 0 and counter == 2: # player rock , comp scissors
    print('You win!')
  elif choice == 1 and counter == 0: # player paper, comp rock
    print('You win!')
  elif choice == 1 and counter == 2: # player paper, comp scissors
    print('You lose!')
  elif choice == 2 and counter == 0: # player scissors, comp rock
    print('You lose')
  elif choice == 2 and counter == 1: # player scissors, comp paper
    print('You win!')

  again = input('Would you like to play again? (y/n) ').lower()

  if again == 'y':
    again = True
  else:
    again = False
    print('Thanks for playing!')
# hangman game
import random
import word_list
import art

# randomly choose word from the list and assign it to variable chosen word
chosen_word = random.choice(word_list.words)
display = ['_' for _ in range(len(chosen_word))]

lives = 6

print(art.logo)
print(f'Chosen word is {chosen_word} ... shhhhh')

# ask user to guess letter and assign their answer to a variable called guess
# make guess lowercase
game_over = False
while not game_over:
  guess = input('Guess a letter: ').lower()

  # check if letter guess is in chosen_word
  for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
      display[i] = chosen_word[i]
  
  if guess not in chosen_word:
    lives -= 1

  if lives == 0:
    print('You Lose!')
    game_over = True

  print(''.join(display))
  print(art.stages[lives])

  if '_' not in display:
    game_over = True
    print('You Win!')

# Caesar cypher program
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

again = True
while again:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  if direction != 'encode' and direction != 'decode':
    print('Please enter \'decode\' or \'encode\' only.')
    again = True
    continue

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text, shift, direction):
    cypher = ''
    for ch in text:
      if ch in alphabet:
        index = alphabet.index(ch)

        if direction == 'encode':
          if index + shift > 25:
            index = (index + shift) - 25 - 1
          else:
            index += shift
        elif direction == 'decode':
          index -= shift
      
        cypher += alphabet[index]
      
      else:
        cypher += ch

    print(f'The {direction}d text is {cypher}')

  caesar(text, shift, direction)

  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  if again == 'yes': 
    again = True 
  else: 
    again = False
import art
import os

# clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(art.logo)
print('Welcome to the secret auction program.')

auction = {}

again = True

while again:
  name = input('What is your name?: ')
  bid = input('What\'s your bid?: $')
  # add to auction 
  auction[name] = bid

  others = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')

  if others == 'yes':
    cls()
    again = True
  else:
    again = False

highest_bid = auction[list(auction.keys())[0]]
highest_bidder = list(auction.keys())[0]

for key in auction:
   if highest_bid < auction[key]:
      highest_bid = auction[key]
      highest_bidder = key
print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')
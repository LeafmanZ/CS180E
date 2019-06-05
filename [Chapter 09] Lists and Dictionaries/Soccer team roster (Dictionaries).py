# Type code here
"""FUNCTION DEFINITIONS"""
def print_menu():
    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit')
#U
def update_rating():
    jersey = int(input('Enter a jersey number:\n'))
    rating = int(input('Enter a new rating for player:\n'))
    players[jersey] = rating
# R
def output_above(players):
    rating = int(input('Enter a rating:\n\n'))
    print('ABOVE', rating)
    sorted_keylist = sorted(players.keys())
    for jersey in sorted_keylist:
        if players[jersey] > rating:
            print('Jersey number: %d, Rating: %d' % (jersey, players[jersey]))
# O            
def output_roster(players):
    print('ROSTER')
    sorted_keylist = sorted(players.keys())
    for jersey in sorted_keylist:
        print('Jersey number: %d, Rating: %d' % (jersey, players[jersey]))

"""Program Begins"""
players = {}
for i in range(1,6):
    jersey = int(input('Enter player %s\'s jersey number:\n' % i))
    rating = int(input('Enter player %s\'s rating:\n\n' % i))
    players[jersey] = rating
    
output_roster(players)
print_menu()

option = input('\nChoose an option:\n')
while option != 'q':
    if option == 'a':
        jersey = int(input('Enter a new player\'s jersey number:\n'))
        rating = int(input('Enter the player\'s rating:\n'))
        players[jersey] = rating
    elif option == 'd':
        jersey = int(input('Enter a jersey number:\n'))
        del players[jersey]
    elif option == 'u':
        update_rating()
    elif option == 'r':
        output_above(players)
    elif option == 'o':
        output_roster(players)
    else:
        print('Wrong input try again.')
    
    print_menu()
    option = input('\nChoose an option:\n')

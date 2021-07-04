# Game of updating a list.

def display_game(current_list):
    print('here is the game list: ', current_list)

def position_choice():
    position = 'Two'
    while not position in range(len(current_list)):
        position = input('Pick a position to replace 0,1,2: ')
        if position.isdigit() and int(position) in range(len(current_list)):
            return int(position)
        else:
            print('Sorry but you did not choose a valid position [0,1,2]')

def replacement_choice(current_list, position):
    value = input('Type a String to place at the position: ')
    current_list[position] = value
    return current_list

def gameon_choice():
    choice = 'Any'
    while choice not in ['Y', 'N']:
        choice = input('Would you like to keep playing? Y or N: ')
        if choice in ['Y', 'N']:
            if choice == 'Y':
                return True
            else:
                return False

game_on = True
current_list = [0, 1, 2]

while game_on:
    display_game(current_list)
    position = position_choice()
    current_list = replacement_choice(current_list, position)
    display_game(current_list)
    game_on = gameon_choice()

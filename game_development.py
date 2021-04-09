# Snake Water Gun Game
import random

abbrebration_dictionary  = {'S': 'Snake',
                            'W': 'Water',
                            'G': 'Gun'}
computer_choice = ['Snake', 'Water', 'Gun']

score_card = {'Human': 0, 'Computer': 0}

def macth_winner_decider(player_1, player_2):
    print(player_1, player_2)
    if player_1 == 'Snake' and player_2 == 'Water':
        score_card['Human'] += 1
        return player_1
    elif player_1 == 'Snake' and player_2 == 'Gun':
        score_card['Computer'] += 1
        return player_2
    elif player_1 == 'Water' and player_2 == 'Gun':
        score_card['Human'] += 1
        return player_1
    elif player_1 == 'Water' and player_2 == 'Snake':
        score_card['Computer'] += 1
        return player_2
    elif player_1 == 'Gun' and player_2 == 'Snake':
        score_card['Human'] += 1
        return player_1
    elif player_1 == 'Gun' and player_2 == 'Water':
        score_card['Computer'] += 1
        return player_2
    elif player_1 == player_2:
        return 'It\'s a draw'


def tournament_winner_decider(score_card):
    if score_card['Human'] > score_card['Computer']:
        print(f'Congratulations you won !!')
    elif score_card['Human'] < score_card['Computer']:
        print(f'Better luck next time !!')
    else:
        print(f'You almost made it to the cross the line')


match_played = 0
while match_played < 3:
    match_played += 1
    human_choice = (input('Choose one of the following: S-Snake, W-Water, G-Gun\n')).capitalize()
    human_choice = abbrebration_dictionary.get(human_choice)
    print(f'{macth_winner_decider(human_choice, random.choice(computer_choice))} \n')
    print(f'{score_card}\n')
tournament_winner_decider(score_card)
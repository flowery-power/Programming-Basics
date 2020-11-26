cards = input()
player_count_a = 11
player_count_b = 11

player_with_card_a = []
player_with_card_b = []

cards = cards.split(" ")
game_was_terminated = False

for card in cards:
    card_list = card.split("-")
    team_name = card_list[0]
    player_number = card_list[1]

    if team_name == "A":
        if player_with_card_a.__contains__(player_number):
            continue
        else:
            player_with_card_a.append(player_number)
            player_count_a -= 1
            if player_count_a < 7:
                print(f"Team A - {player_count_a}; Team B - {player_count_b}")
                print("Game was terminated")
                game_was_terminated = True
                break

    if team_name == "B":
        if player_with_card_b.__contains__(player_number):
            continue
        else:
            player_with_card_b.append(player_number)
            player_count_b -= 1
            if player_count_b < 7:
                print(f"Team A - {player_count_a}; Team B - {player_count_b}")
                print("Game was terminated")
                game_was_terminated = True
                break

if not game_was_terminated:
    print(f"Team A - {player_count_a}; Team B - {player_count_b}")




player_games = {
    "Raj": ["Cricket", "Football"],
    "Alex": ["Football", "Volleyball"],
    "John": ["Cricket", "Throwball"],
    "Doe": ["Throwball"]
}

game_players = {}

for player, games in player_games.items():
    # print(player,games)
    for game in games:
        if game not in game_players:
            game_players[game] = []
        game_players[game].append(player)
print(game_players)
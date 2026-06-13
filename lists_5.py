# num = list(range(1,101))
# squares = [num**2 for num in range(1,101)]
# print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:2])
print(players[-2:])

for player in players[:2]:
    print(player.upper())
    
stars = players

players.append("chandra")
print (stars)

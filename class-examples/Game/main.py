from player import Player

puja = Player("Puja")
puja.lives -= 1
print(puja)

puja.score += 225
puja.level += 2
print(puja)

puja.level -= 1
print(puja)

puja.score = 500
print(puja)

#program to print the list

players = [7,18,1,46,47]

print(players)
players[:2] = [6,9,14] #it replaces the items in the list till second position
print(players)
print(players[:3]) #it prints the elements in lists till third position
print(players[2:]) #it prints the elements in lists from second position
print(players[:-1]) #it prints the elements in lists till second last position
print(players[:])
print(players)

iplayers= players + [57,58,59] #by using '+' it add the elements in the list
print(iplayers)
iplayers = iplayers + [27,28]
print(iplayers)
print(iplayers[:4])
print(iplayers)

print(iplayers)
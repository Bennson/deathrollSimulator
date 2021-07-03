import random

nMax = 50
iterations = 5000
players = ["A", "B"]

playerCurrent = 0
winA = 0
winB = 0

for i in range(iterations):
    nCurrent = nMax
    playerCurrent = 0

    while nCurrent > 1:
        nCurrent = random.randint(1, nCurrent)
        playerCurrent += 1
        print(nCurrent, players[playerCurrent % 2])

    if players[(playerCurrent-1) % 2] == "A":
        winA += 1
    else:
        winB += 1
    print ("Runde ", i, " Sieger Player: ", players[(playerCurrent-1) % 2])

print ("Siege A: ", winA, " Siege B: ", winB)
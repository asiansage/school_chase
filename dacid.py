from random import randint

win = 0
lose = 0
draw = 0
for i in range(10000):
    dacid = randint(8, 15)
    team = randint(20, 40) - dacid
    opponent = randint(15, 35)
    if team > opponent:
        win += 1
    elif team < opponent:
        lose += 1
    else:
        draw += 1
print("Wins without David: ", win)
print("Losses without David: ", lose)
print("Draws without David: ", draw)

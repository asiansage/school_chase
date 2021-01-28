from random import randint

win = 0
lose = 0
draw = 0
for i in range(10000):
    zaien = randint(6, 12)
    team = randint(20, 40) - zaien
    opponent = randint(15, 35)
    if team > opponent:
        win += 1
    elif team < opponent:
        lose += 1
    else:
        draw += 1
print("Wins without Zalian: ", win)
print("Losses without Zalian: ", lose)
print("Draws without Zalian: ", draw)

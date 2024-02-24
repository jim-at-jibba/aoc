import os

if os.path.exists("input.txt"):
    file = open("input.txt").read().rstrip()

    test = "()())"
    up = 0
    down = 0
    floor = 0
    count = 0
    for a in file:
        if a == ")":
            down = down + 1
        else:
            up = up + 1

        count = count + 1
        if down > up:
            print(count)
            break

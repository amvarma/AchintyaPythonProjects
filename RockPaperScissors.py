from random import randint
GameDict = {"r": 1, "p": 2, "s": 3}
inv_map = {v: k for k, v in GameDict.items()}
PlayerMoveChar = str(input("Choose one of the follow:rock(r),paper(p),scissors(s)"))
PlayerMoveInt = GameDict[PlayerMoveChar]
ComputerMove = randint(1, 3)
print(PlayerMoveChar, " ")
print(inv_map[ComputerMove])
if PlayerMoveInt == ComputerMove:
    print("DRAW")
elif PlayerMoveInt > ComputerMove:
    if PlayerMoveInt == 2:
        print("Player Wins")
    elif PlayerMoveInt == 3:
        if ComputerMove == 2:
            print("Player Wins")
        else:
            print("Computer Wins! :(")
else:
    if PlayerMoveInt == 2:
        print("Computer Wins")
    else:
        if ComputerMove==2:
            print("Computer Wins")
        else:
            print("Player Wins!")






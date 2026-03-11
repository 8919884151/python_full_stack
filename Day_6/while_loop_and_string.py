'''#while loop

i=1
while i<=10:
    print(i)
    i=i+1

i=5
while i>0:
    print(f"{i} are left!you can shoot")
    i=i-1
else:
    print("Game over")

moves=20
winning_move=18
while moves>0:
    if moves==winning_move:
        print("You win the game")
        break
    print(f"{moves} moves are left!")
    moves=moves-1
else:
    print("Game over")'''






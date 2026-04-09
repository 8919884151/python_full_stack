import random
def dice():
    return random.randint(1,6)

p1=input("Enter player 1: ")
p2=input("Enter player 2: ")
ps1,ps2=0,0
winning_point=100
ladders={6:25,12:31,35:90,46:60,51:74,78:99,82:96}
snakes={24:5,45:18,66:33,74:37,88:77,93:57,98:21}

while ps1<winning_point and ps2<winning_point:
    s1=input(f"{p1}:[P]lay or [Q]uit: ").lower()
    if s1=='p':
        dice_1=dice()
        print(f"Dice score: {dice_1}")
        ps1+=dice_1
        if ps1 in ladders:
            ps1=ladders[ps1]
            print(f"++++++Ladder-Board score: {ps1}")
        elif ps1 in snakes:
            ps1=snakes[ps1]
            print(f"------Snake bite-Board score: {ps1}")
        elif (ps1+dice_1)==winning_point:
            print(f"{p1} won the game")
            break
        else:
            print(f"Board score: {ps1}")
        #if ps1>100:
           # ps1=ps1-dice_1
           #continue
    elif s1=='q':
        print(f"{p2} won the game")
        break
    else:
        print("Enter the valid input")

    s2=input(f"{p2}:[P]lay or [Q]uit: ").lower()
    if s2=='p':
        dice_2=dice()
        print(f"Dice score: {dice_2}")
        ps2+=dice_2
        if ps2 in ladders:
            ps2=ladders[ps2]
            print(f"++++++Ladder-Board score: {ps2}")
        elif ps2 in snakes:
            ps2=snakes[ps2]
            print(f"------Snake bite-Board score: {ps2}")
        elif (ps1+dice_1)==winning_point:
            print(f"{p1} won the game")
            break
        else:
            print(f"Board score: {ps2}")
    
         
    elif s2=='q':
        print(f"{p1} won the game")
        break
    else:
        print("Enter the valid input")

if ps1>ps2:
    print(f"********{p1} won the game")
else:
    print(f"********{p2} won the game")




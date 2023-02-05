import random
num = random.randint(1,10)
for i in range(5):
    gnum = int(input("Guess a number: "))
    if gnum < num:
        print("wrong guess, try a greater number. Live left for guess ",5-i-1)
    elif gnum > num:
        print("wrong guess, try a lesser number. Live left for guess ",5-i-1)
    else:
        print("Congratulation, you have guessed the number in ",i+1," attempt.")
        break
    while (5-i-1)==0:
        print("Game Over.")
        break

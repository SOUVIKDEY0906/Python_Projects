import random

while True:
    choices = ['rock', 'paper', 'scissor']
    com = random.choice(choices)
    player = input("Rock, Paper or Scissor? : ").lower()


    while player not in choices:
        player = input("Rock, Paper or Scissor? : ").lower()

    if player == com:
        print("YOU : ", player)
        print("BOT : ", com)
        print("Tie!")
    elif player == 'rock':
        if com == 'paper':
            print("BOT : ", com)
            print("YOU : ", player)
            print("You Lose! :(")
        if com == 'scissor':
            print("BOT : ", com)
            print("YOU : ", player)
            print("You Won! :)")
    elif player == 'paper':
        if com == 'scissor':
            print("BOT : ", com)
            print("YOU : ", player)
            print("You Lose! :(")
        if com == 'rock':
            print("BOT : ", com)
            print("YOU : ", player)
            print("You Won! :)")
    elif player == 'scissor':
        if com == 'rock':
            print("BOT : ", com)
            print("YOU : ", player)
            print("You Lose! :(")
        if com == 'paper':
            print("BOT : ", com)
            print("YOU : ", player)
            print("You Won! :)")
         
    play_again = input("Want to play again?(y/n) :").lower()
    if play_again != 'y':
        break

print("Have a nice day!")
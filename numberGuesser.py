import random
def restart():
    choice = input("Do you want to restart the game? (y/n)\n")
    if(choice.lower() == 'y'):
        TheGame()
    return
def TheGame():
    correct_answer = random.randint(1, 50)
    result = 0
    chances = 5
    hint = "Guess a Number!"
    while(chances):
        print("Remaining Chances: ", chances)
        print("Hint: ", hint)
        guess = int(input("Enter your guess: "))
        if(guess > correct_answer):
            hint = "Correct answer is lower!"
        elif(guess < correct_answer):
            hint = "Correct answer is higher!"
        else:
            result = 1
            break
        chances -= 1
    if(result):
        print("You Win!")
    else: 
        print("You Lose!")
    restart()
TheGame()
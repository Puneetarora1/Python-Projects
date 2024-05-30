import random

def GuessTheNumber():
    randomNo = random.randint(1,101)
    # print(randomNo)
    guesses = 0
    while True:
        userInput = int(input("Enter Your Number :- "))
        if userInput > randomNo:
            guesses += 1
            print('Please enter a small no.')
            print(f'You have taken {guesses} guesses')
        elif userInput == randomNo:
            guesses += 1
            print(f'Congratulation, You entered right no {randomNo}')
            print(f'You took total {guesses} guesses')
            break
        else:
            guesses += 1
            print("Please enter a big no.")
            print(f'You have taken {guesses} guesses')
        
        if guesses == 11:
            print("You took your all guesses")
            print("game over")
            print(f"Required Number was {randomNo}")
            break
    return guesses


minC = GuessTheNumber()
# print(f'Value of minC is {minC}')

with open('minGuessesGTM_Game.txt', 'r') as f:
    minG = f.read()

if minG == '' or minC < int(minG):
    print(f'You have taken least Guesses {minC}')
    with open('minGuessesGTM_Game.txt', 'w') as f:
        f.write(str(minC))
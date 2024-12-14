import random

# Print multiline instruction
print("===========ROCK PAPER SCISSOR===========")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")


    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        USER = 'Rock'
    elif choice == 2:
        USER = 'Paper'
    else:
        USER = 'Scissors'

    print('User choice is:', USER)

    print("...")

    COMPUTER = random.randint(1, 3)
    if COMPUTER == 1:
        COMPUTER_CHOICE = 'Rock'
    elif COMPUTER == 2:
        COMPUTER_CHOICE = 'Paper'
    else:
        COMPUTER_CHOICE = 'Scissors'

    print("Computer choice is:", COMPUTER_CHOICE)
    print(USER, 'vs',COMPUTER_CHOICE)

    if choice == COMPUTER_CHOICE:
        result = "DRAW"

    elif (choice == 1 and COMPUTER  == 2) or (COMPUTER  == 1 and choice == 2):
        result = 'Paper'

    elif (choice == 1 and COMPUTER  == 3) or (COMPUTER  == 1 and choice == 3):
        result = 'Rock'
        
    elif (choice == 2 and COMPUTER  == 3) or (COMPUTER  == 2 and choice == 3):
        result = 'Scissors'

    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == USER:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    play=input(print("Do you want to play again? (Y/N)"))
    if play == "N":
        break
    if play == 'Y':
        break

print("Thanks for playing! ")
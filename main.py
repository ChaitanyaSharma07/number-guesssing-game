import random

global guesses

#giving the player an option to decide the range for the number

try: 
    range_num = int(input("Enter a number till which you would like a random number to be generated: "))
except:
    print("You entered an incorrect value")
    print("Please try again")
    range_num = int(input("Enter a number till which you would like a random number to be generated: "))

#declaring variables
guessing_number = random.randint(1, range_num)

#showing input for number of players
player_inp = input("Enter the number of players(one, two): ")

#main game loop for single player
def player_1():
    guesses = 0
    while guesses < 5:
        global num_inp

        try: 
            num_inp = int(input("Enter a number between 1 and " + str(range_num) +  ": "))
        except ValueError:
            print("Please try again, you entered a wrong value")
            num_inp = int(input("Enter a number between 1 and " + str(range_num) +  ": "))

        #checking whether the number is equal or not
        if num_inp < guessing_number:
            print("your guess is lower than the number")
            print("-----------------------------------------------------")
            guesses += 1
        elif num_inp > guessing_number:
            print("Your number is greater than the guessing number")
            print("-----------------------------------------------------")
            guesses += 1
        elif num_inp == guessing_number:
            print("You have won!!")
            print("-----------------------------------------------------")
            break


    if not guesses < 5 and player_inp == "one":
        print("You lost, player 1 the number was " + str(guessing_number))

#function for player 2
def player_2():
    guesses = 0
    while guesses < 5:
        global num_inp

        try: 
            num_inp = int(input("Enter a number between 1 and " + str(range_num) +  ": "))
        except ValueError:
            print("Please try again, you entered a wrong value")
            num_inp = int(input("Enter a number between 1 and " + str(range_num) +  ": "))

        #checking whether the number is equal or not
        if num_inp < guessing_number:
            print("your guess is lower than the number")
            print("-----------------------------------------------------")
            guesses += 1
        elif num_inp > guessing_number:
            print("Your number is greater than the guessing number")
            print("-----------------------------------------------------")
            guesses += 1
        elif num_inp == guessing_number:
            print("You have won!!")
            print("-----------------------------------------------------")
            break


    if not guesses < 5:
        print("You lost, player 2, the number was " + str(guessing_number))


#function for multiplayer
def multi_player():
    global overall_guesses
    overall_guesses = 0

    #main loop for multi_player
    while overall_guesses <= 10:
        print("Now player 1's turn")
        player_1()
        overall_guesses += 1
        print("--------------------------------------")
        print("Now player 2's turn")
        player_2()
        overall_guesses += 1
        print("-------------------------")








if player_inp == "one":
    player_1()
elif player_inp == "two":
    multi_player()




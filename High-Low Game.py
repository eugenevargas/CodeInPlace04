import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    #Initialize round and score
    round_num = 1
    user_score = 0

    while round_num <= NUM_ROUNDS:
        #Generate random numbers
        user_num = random.randint(1,100)
        computer_num = random.randint(1,100)

        #Print round number, ask user input
        print(f"Round {round_num}")
        print(f"Your number is {user_num}")
        user_choice = input("Do you think your number is higher or lower than the computer's? ")
        
        #Validate user input
        while user_choice != "Higher" and user_choice != "Lower":
            user_choice = input("Please enter Higher or Lower. ")

        #If user number is less than computer number
        if user_choice == "Lower" and user_num < computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            user_score +=1
        elif user_choice == "Higher" and user_num < computer_num:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        
        #If user number is greater than computer number
        elif user_choice == "Lower" and user_num > computer_num:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")
        elif user_choice == "Higher" and user_num > computer_num:
            print(f"You were right! The computer's number was {computer_num}")
            user_score +=1

        #If user number and computer number are equal
        elif user_num == computer_num:
            print(f"Both your numbers are {user_num}! No points for anyone.")


        print(f"Your score is now {user_score}")

        #Increment round number
        round_num += 1
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
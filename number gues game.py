# 


import random





def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1




            if guess < 1 or guess > 100:
                print("Please guess a number **within** the range 1-100.")
                continue




            if guess < number_to_guess:
                print("Try something higher than that!!.")
            elif guess > number_to_guess:
                print("try something lower than that.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()

import random

print("Think of a secret number between 1 and 10! 🤔")
secret_number = int(input("Enter your secret number (The computer will try to guess it): "))

computer_guess = random.randint(1, 10)
print(f"Computer's first guess is: {computer_guess}")

while True:
    feedback = input("Is this guess correct? (higher/lower/correct): ").lower()

    if feedback == "correct":
        print("Yay! 🎉 The computer guessed correctly! ✅")
        break  # Exit loop if the guess is correct
    elif feedback == "higher":
        print("Too high!")
    elif feedback == "lower":
        print("Too Low!")
    else:
        print("Invalid input! Please type only 'higher', 'lower', or 'correct'.")
        continue  # Restart loop if input is incorrect

    computer_guess = random.randint(1, 10)  # Generate a new guess
    print(f"Computer's new guess is: {computer_guess}")

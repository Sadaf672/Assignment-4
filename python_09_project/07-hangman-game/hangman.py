import random
words_list = ["code","python","hangman"]

def display_word(word,guessed):
     display = ""
     for letter in word:
        if letter in guessed:
          display += letter
        else:
          display += "_"
        display += " "
     return display

word = random.choice(words_list)
def hangman():
     guessed_letters = set()
     attempts = 6
     while attempts > 0:
        print("-"*20)
        print("Welcome to Hangman Game")
        print(f"word : {display_word(word=word,guessed=guessed_letters)}")
        print(f"Guessed Letter: {' '.join(guessed_letters)}")
        print(f"Remaining Attempts : {attempts}")

        guess = input("Enter The Letter: ").lower()
        guessed_letters.add(guess)

        if guess in word:
          print("Good Guess!")
        else:
          print("Wrong Guess!")
          attempts -= 1

        if "_" not in display_word(word,guessed_letters):
          print("Congratulaions you won")
          print(f"The Word Was :{word}")
          break

     else:
        print("You Failed")

if __name__ == "__main__":
    hangman()
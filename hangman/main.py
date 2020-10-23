import random


class Hangman:
    food = ["pizza", "hamburger", "strawberry", "popsicle", "spaghetti", "ice cream", "fish and chips", "muffin"]
    movies = ["star wars", "the titanic", "avatar", "indiana jones", "the godfather", "beauty and the beast", "a clockwork orange"]
    animals = ["horse", "goldfish", "goose", "rabbit", "mountain goat", "elephant", "giraffe", "penguin"]

    # lists of words to pick from for each game mode
    # more game modes and words per game mode can be easily added (maybe make functionality so no statements testing every game mode

    def __init__(self):
        self.game_mode = None
        self.lives = 6
        self.word = None
        self.letter_bank = []  # every letter the user guesses
        self.correct_guesses = []  # every correct letter the user guesses. Used to check if they got the word
        self.num_guesses = 0

    def get_word(self):
        while True:
            self.game_mode = input("Select a game mode! (food, movies, animals)\n").casefold()
            if self.game_mode == "food":
                word_list = self.food
                self.word = random.choice(word_list)
                break
            elif self.game_mode == "movies":
                word_list = self.movies
                self.word = random.choice(word_list)
                break
            elif self.game_mode == "animals":
                word_list = self.animals
                self.word = random.choice(word_list)
                break
            elif self.game_mode == "exit":
                print("Sad to see you go :(")
                quit()
            else:
                print("Sorry, I did not understand that. The game modes are food, movies, and animals\n")
                continue
        print()
        for i in self.word:
            if i == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")

    def reset_game(self):
        self.lives = 6
        self.num_guesses = 0
        self.letter_bank.clear()
        self.correct_guesses.clear()

    def loop(self):
        while True:
            response = input("Do you want to play again?\n").casefold()
            if response == "yes":
                print()
                self.reset_game()
                self.get_word()
                self.play()
            elif response == "no":
                print("Have a great day!")
                quit()  # it asks if you want to play again twice after the first replay so quit solves that
            elif response == "exit":  # unnecessary but to follow what computer said in intro
                print("Have a great day!")
                quit()
            else:
                print("Sorry, I did not understand that. Please type yes or no.\n")
                continue

    def play(self):
        while True:
            guess = input("\nGuess a letter or the phrase:\n").casefold()
            if guess == "exit":
                print("Sad to see you go :(")
                quit()
            if guess == self.word:
                self.num_guesses += 1
                print(f"\nYou won! You have {self.lives} lives left and it took you {self.num_guesses} guesses.\n")
                self.loop()
                break
            elif guess in self.letter_bank:
                print("You already guessed that.")
                continue
            print()
            self.num_guesses += 1
            self.letter_bank.append(guess)
            if guess not in self.word:
                self.lives -= 1
            else:
                self.correct_guesses.append(guess)
            for i in self.word:
                if i in self.correct_guesses:
                    print(i, end=" ")
                elif i == " ":
                    print(" ", end=" ")
                else:
                    print("_", end=" ")
            if set(self.correct_guesses) == set(self.word.replace(" ", "")):
                print(f"\nYou won! You have {self.lives} lives left and it took you {self.num_guesses} guesses.\n")
                self.loop()
                break
            if self.lives == 0:
                print(f"\nYou lost! The word was {self.word}.\n")
                self.loop()
                break
            print("\nLetters Bank:", self.letter_bank)
            print("Lives Left:", self.lives, "")

    def run_game(self):
        print('''
        *********************
            Hangman Game!
        *********************
        ''')
        self.get_word()
        self.play()

    def run_game_intro(self):  # thought it would be fun to have an intro
        print("Hello! I am a computer. What's your name?")
        name = input().title()
        print(f"Hello {name}! Are you ready to play hangman?")
        while True:
            response = input().casefold()
            if response == "yes":
                print("Great! Type exit at any time to quit.")
                self.run_game()
                break
            elif response == "no":
                print("See you another time!")
                break
            else:
                print("Sorry, I didn't understand that. Please type yes or no.")
                continue


your_hangman = Hangman()
your_hangman.run_game_intro()

# is using quit() instead of break okay? Did it when using break was too complicated
# note: I'm following OOP paradigm. I'm sure that this isn't necessary and won't have anu special functions.
# but it does seem a lot more logical and organised to me now. yippee OOP!

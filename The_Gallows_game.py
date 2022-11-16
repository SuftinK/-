import Classes

"""This is the main program of the game"""
def choise_check():
    ch = input("Print 1 or 2: ")
    if ch in ["1", "2"] and len(ch) == 1:
        return ch
    else:
        print("The wrong input. Pleas try one's again", end=" ")
        choise_check()

def user_letter_check(step:int, word):
    letter = input(f"\nThis is your {numbering_dict.get(step, 'some')} try. "
                       f"Print your letter: ")
    if letter.isalpha() and len(letter) == 1:
        word.letter = letter
        word.open_the_new_letters()
        print(word)
        return
    else:
        print(f"The uncorrect input, please try one's again. Use only one letter")
        user_letter_check(step, word)

def word_check(word:str):
    answer = input(f"Please print the hole word: ").upper()
    if answer.isalpha():
        return True if answer == word else False
    else:
        print(f"The wrong input. Please one more try.")
        word_check(word)

# Support dictionary
numbering_dict = {
    1:"first",
    2:"second",
    3:"third",
    4:"fourth",
    5:"fifth",
    6:"sixth and final"
}

word = Classes.Tablo("Паравоз")
print(f'Welcome to our game named "The Gallows game" \n'
      f'Your task is guess the hidden word. \n'
      f'Please note, you have only 6 trys,\n'
      f'after that the game will over.\n'
      f'Be brave and good luck')
print(f"\n{word}")

for step in range(1, 7):
    user_letter_check(step, word)
    if "*" not in word._hidden or step == 6:
        break
    print("Will you print the hole Word (1) or choose one more Letter (2)?", end=" ")
    ch = choise_check()
    if ch == "2":
        print("Ok, continue the game")
        continue
    elif ch == "1":
        if word_check(word._word):
            print(f"Congratulation!!! you are perfectly right! the hidden word was {word._word}")
            break
        else:
            print(f"Thank you for game! Have a nice day.")
            break
if "*" in word._hidden:
    if word_check(word._word):
        print(f"Congratulation!!! you are perfectly right! the hidden word was {word._word}")
    else:
        print(f"Unfortunately you loose all you try's and final version was wrong :-( "
              f"Your life is over.")

print("Game over.")

# word.letter = "а"
# word.open_the_new_letters()
# print(word)

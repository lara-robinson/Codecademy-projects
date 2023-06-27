import random

#A list of random words
list_of_words = [
  "CATHEDRAL",
  "MOMENT",
  "POSTURE",
  "PARTICIPATE",
  "RECEPTION",
  "LIABILITY",
  "ARTIST",
  "ACCURATE",
  "HELICOPTER",
  "VOUCHER",
  "GLACIER",
  "GENERAL",
  "ELEPHANT",
  "SUSPECT",
  "PROPERTY",
  "MATRIX",
  "DICTIONARY",
  "DIPLOMATIC",
  "CONTACT",
  "PUNISH",
  "AMBITION",
  "EXPLORATION",
  "OMISSION",
  "SAMPLE",
  "RETAIN",
  "MATTER",
  "ANNUAL",
  "RETURN",
  "MYSTERY",
  "COMPLICATION",
  "MOSQUITO",
  "REMARK",
  "GOVERNMENT",
  "DISAPPEAR",
  "ILLNESS",
  "ORIGINAL",
  "FORMULATE",
  "OFFENDER",
  "RELIABLE",
  "INJURY",
  "INSTALL",
  "VALLEY",
  "NUANCE",
  "LEGISLATION",
  "CONTRAST",
  "ARRANGEMENT",
  "RECESSION",
  "WRIGGLE",
  "CRYSTAL",
  "SUNTAN"]

#Turning the list of strings into a 2d list where each string is turned into a list of its letters. TODO: Consider refactoring the code below so I don't need this step  
def create_2d_list_of_words(list_of_words):
  new_list_of_words = [[] for word in list_of_words]
  index = 0
  for word in list_of_words:
    for i in range(len(word)):
      new_list_of_words[index].append(word[i])
    index += 1
  return new_list_of_words

#Assigning the 2d list to a variable
new_list = create_2d_list_of_words(list_of_words)

#Game Intro
print("Welcome to my Python terminal game. You can play hangman, right from the comfort of your own terminal. You must guess the secret word one letter at a time. Six wrong guesses and you're hanged!",'\n')

#Selecting a random "secret word" for the game from the 2d list of words
length_of_list_of_words = len(new_list) -1
random_number = random.randint(0,length_of_list_of_words)
secret_word = new_list[random_number]

#Count the letters in the "secret word" to create the placeholder where correct guesses will appear 
secret_word_holder = ['_' for _ in range(len(secret_word))]

#More game intro
print("Here is the word you need to guess:","\n")
print(" ".join(secret_word_holder))


#Assigning the number of wrong guesses and initializing the wrong letter bank
wrong_guesses_left = 6
wrong_letter_list = []

#This function checks if the letter guessed by the player is in the secret word. The guessed letter fills in the empty slots in the word holder whereever the letter occurs. If the letter does not occur, the player loses a wrong guess and the letter is added to the wrong letter bank. TODO: Refactor this so its less chunky
def evaluate_guess(letter_guess):
  index = 0
  if letter_guess in secret_word:
    for letter in secret_word:
        if letter == letter_guess:
            secret_word_holder[index] = letter_guess
            index += 1
        else:
          index += 1
    return print("\n",letter_guess, "is in the secret word!","\n", " ".join(secret_word_holder),"\n", "Wrong guesses:", ", ".join(wrong_letter_list))
  if letter_guess not in secret_word:
    global wrong_guesses_left 
    wrong_guesses_left -= 1
    wrong_letter_list.append(letter_guess)
    if wrong_guesses_left != 1: 
      return print("\n","Boo!", letter_guess, "is not in the secret word!","\n", "You have {guess} wrong guesses left".format(guess=wrong_guesses_left),"\n", "Wrong guesses:", ", ".join(wrong_letter_list),"\n", " ".join(secret_word_holder))
    if wrong_guesses_left == 1: 
      return print("\n","Boo!", letter_guess, "is not in the secret word!","\n", "You have {guess} wrong guess left".format(guess=wrong_guesses_left),"\n", "Wrong guesses:", ", ".join(wrong_letter_list),"\n", " ".join(secret_word_holder))

#The actual gameplay
while wrong_guesses_left > 0 and secret_word != secret_word_holder:
  print("\n","Guess your letter:")
  letter_guess = input()
  letter_guess = letter_guess.upper()
  evaluate_guess(letter_guess)

#Check to see if the player won the game
if secret_word == secret_word_holder:
  final_word = "".join(secret_word)
  print("\n",final_word,"is the correct answer! Great job!")

#Check to see if the player lost the game
if wrong_guesses_left == 0:
  final_word = "".join(secret_word)
  print("\n","X_X Game over, man! The secret word was:", final_word)

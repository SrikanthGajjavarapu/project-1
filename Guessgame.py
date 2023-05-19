#Guessgame
import random
name=input("what is your name?")
print("good luck!",name)
words=["python","student","play","car","gym","sleep","book","library","delhi","lab"]
word=random.choice(words)
print("guess the character")
guesses=" "
turns=15
while turns>0:
  failed=0
  for char in word:
    if char in guesses:
      print(char)
    else:
      print("_")
      failed+=1
  if failed==0:
    print("you win!")
    print("the word is",word)
    break
  guess=input("enter your character")
  guesses+=guess
  if guess not in word:
    turns-=1
    print("wrong")
    print("you have",+turns,"more guesses")
  if turns==0:
    print("you loose!")
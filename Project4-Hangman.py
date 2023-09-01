from random import choice

def run_game():
    word=choice(["hello","name","Tharun"])

    name=input("Enter your name:")
    print(f"welcome to the game Hangman: {name}")

    guessed_chars=""
    tries=3
    cheat=1

    while tries>0:
        blanks=0
        print("Word: ",end="")
        for char in word:
            if char in guessed_chars:
                print(char,end="")
            else:
                print("_",end="")
                blanks+=1
        print()
        if(blanks==0):
            print("You got it")
            break
        guess_the_letter=input("Enter a letter: ")
        if(len(guess_the_letter)>1):
            if(cheat==1):
                print("U r trying cheat...Final Warning")
                cheat-=1
                continue
            else:
                print("You have cheated more than once..You are out od the game")
                break
        if(guess_the_letter in guessed_chars):
            print("You have used the letter....dont waste your time")
            continue
        #adding the letter to the previous guessed letter
        guessed_chars+=guess_the_letter
        if guess_the_letter not in word:
            tries-=1
            print("You have guessed wrong letter...{tries} tries remaining")

            if tries==0:
                print("Sorry...You have Lost!")
                break







if __name__=="__main__" :   
    run_game()

#random rock paper scissors
import random
import sys
import time

list1= ["1", "2", "3"]
score1 = 0
score2 = 0

# user input
while True:
    computer_choice = random.choice(list1)
    user_choice = input("Which one do you choose? Enter \n \n 1 for rock\n 2 for paper or\n 3 for scissors\n")
    time.sleep(1)
    if user_choice == computer_choice:
        print("Tie!")
        time.sleep(1)
    elif user_choice == "1" and computer_choice == "2":
        print("You chose \"rock\". The computer chose \"paper\".\nThe computer won!")
        score2 += 1
        time.sleep(2)
        print(f"\nYour score: {score1}\nComputers' score: {score2}")
        time.sleep(1)
    elif user_choice == "1" and computer_choice == "3":
        print("You chose \"rock\". The computer chose \"scissors\".\nYou won!")
        score1 += 1
        time.sleep(2)
        print(f"\nYour score: {score1}\nComputers' score: {score2}")
        time.sleep(1)
    elif user_choice == "2" and computer_choice == "1":
        print("You chose \"paper\". The computer chose \"rock\".\nYou won!")
        score1 += 1
        time.sleep(2)
        print(f"\nYour score: {score1}\nComputers' score: {score2}")
        time.sleep(1)
    elif user_choice == "2" and computer_choice == "3":
        print("You chose \"paper\". The computer chose \"scissors\".\nThe computer won!")
        score2 += 1
        time.sleep(2)
        print(f"\nYour score: {score1}\nComputers' score: {score2}")
        time.sleep(1)
    elif user_choice == "3" and computer_choice == "1":
        print("\nYou chose \"scissors\". The computer chose \"rock\".\nThe computer won!")
        score2 += 1
        time.sleep(2)
        print(f"\nYour score: {score1}\nComputers' score: {score2}")
        time.sleep(1)
    elif user_choice == "3" and computer_choice == "2":
        print("You chose \"scissors\". The computer chose \"paper\".\nYou won!")
        score1 += 1
        time.sleep(2)
        print(f"\nYour score: {score1}\nComputers' score: {score2}")
        time.sleep(1)
    else: 
        print("Invalid input")

    while True:
        time.sleep(1)
        print("")
        continue1 = input("Do you want to continue? Enter y or n\n") 
        if continue1 == "y":
            break
        elif continue1 =="n":
            print("Bye!")
            sys.exit()
        else:
            print("Invalid value")



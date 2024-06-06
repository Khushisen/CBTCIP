import random
print("Type 0 for Rock")
print("Type 1 for paper")
print("Type 2 for scissor")
user = int(input("Enter your choice : "))
if user >= 3 or user < 0:
    print("Invalid number. Choose from 0, 1, 2 only.")
else :
    computer = random.randint(0,2)
    print("Computer choose : ")
    print(computer)
    if computer == user:
        print("Its a draw")
    elif computer == 0 and user == 2:
        print("You lose")
    elif user == 0 and computer == 2:
        print("You win")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You win")


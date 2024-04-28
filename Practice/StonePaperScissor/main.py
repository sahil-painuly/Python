import random

def winner(user, comp):
    rules = {1: 3, 2: 1, 3: 2}  
    if user == comp:
        return 0  
    elif rules[user] == comp:
        return 1  
    else:
        return -1  

print("\nR\tU\tL\tE\tS\n\nRock->1\tPaper->2\tScissor->3\n")

while True:
    try:
        user = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissor): "))
        if user not in [1, 2, 3]:
            print("Wrong value! Please enter a value based on the given rules.")
        else:
            break
    except ValueError:
        print("Wrong value entered by user! Please enter a number.")

rules = {1: "Rock", 2: "Paper", 3: "Scissor"}

comp = random.randint(1, 3)

win = winner(user, comp)

if win == 0:
    print(f"You chose {rules[user]} and the system chose {rules[comp]}, so it's a draw.")
elif win == 1:
    print(f"You chose {rules[user]} and the system chose {rules[comp]}, so you win!")
else:
    print(f"You chose {rules[user]} and the system chose {rules[comp]}, so you lose!")

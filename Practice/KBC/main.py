import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rules():
    levels = {
        "Level1": "500",
        "Level2": "700",
        "Level3": "1000",
        "Level4": "1500",
        "Level5": "2000",
        "Level6": "5000",
        "Level7": "10000",
        "Level8": "15000",
        "Level9": "20000",
        "Level10": "25000"
    }
    return levels

qlist = [
    "Who is known as the 'Father of Computers'?\na.Charles Babbage\tb.Alan Turing\nc.Steve Jobs\td.Bill Gates",
    "What is the capital of France?\na.London\tb.Paris\nc.Berlin\td.Rome",
    "Which planet is known as the 'Red Planet'?\na.Venus\tb.Mars\nc.Jupiter\td.Saturn",
    "What is the largest mammal?\na.Elephant\tb.Whale\nc.Hippo\td.Giraffe",
    "Who wrote 'Romeo and Juliet'?\na.William Shakespeare\tb.Jane Austen\nc.Charles Dickens\td.Mark Twain",
    "What is the currency of Japan?\na.Yuan\tb.Yen\nc.Dollar\td.Euro",
    "Which gas do plants absorb during photosynthesis?\na.Oxygen\tb.Hydrogen\nc.Nitrogen\td.Carbon dioxide",
    "What is the tallest mountain in the world?\na.Mount Everest\tb.K2\nc.Kangchenjunga\td.Makalu",
    "Which country is famous for the Great Wall?\na.India\tb.China\nc.Russia\td.Brazil",
    "What is the chemical symbol for water?\na.H2O\tb.CO2\nc.NaCl\td.C6H12O6"
]

questions = {
    qlist[0]: "a",
    qlist[1]: "b",
    qlist[2]: "b",
    qlist[3]: "b",
    qlist[4]: "a",
    qlist[5]: "b",
    qlist[6]: "d",
    qlist[7]: "a",
    qlist[8]: "b",
    qlist[9]: "a"
}

ch = input('Are you want to play KBC (Kon Banega Crorepati)!!\na. yes\tb. no\n')

if ch.lower() == "yes":
    clear_screen()
    choice = int(input("For KBC Rules Press 1 otherwise Press any digit to continue.\nThanks.\n"))
    if choice == 1:
        levels = rules()
        for key, value in levels.items():
            print(f"{key} -> Rs.{value}")
    
    ch = input("Do you want to proceed? (yes/no): ")
    while ch.lower() not in ["yes", "no"]:
        print("Invalid input! Please enter 'yes' or 'no'.")
        ch = input("Do you want to proceed? (yes/no): ")

    if ch.lower()=="yes":
        winnings = [int(value) for value in rules().values()]
        total_winnings = 0

        for i in range(10):
            clear_screen()  # Clear the screen
            if i > 0:
                print(f"{i+1} Question ye raha Apki computer screen par-->")
            else:
                print("Welcome to the game!\nPhela Question ye raha Apki computer screen par-->")

            print(qlist[i])
            ans = input("Answer(a, b, c, d): ")

            correct_ans = questions[qlist[i]]

            if ans.lower() == correct_ans:
                total_winnings += winnings[i]
                print(f"Correct answer! You've won Rs. {winnings[i]} for this question and a total of Rs. {total_winnings} so far.")
                if i < 9:
                    next_question = input("Do you want to proceed to the next question? (yes/no): ")
                    if next_question.lower() != "yes":
                        break
            else:
                print(f"Wrong answer! Correct answer was: {correct_ans}")
                print(f"Your total winning amount is Rs. {total_winnings}")
                break  
        

else:
    print("Exiting... Thank you for coming!")


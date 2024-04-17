# A simple interactive billing system that allows users to input
# item prices and calculates the total bill.
# The program should repeatedly prompt the user to enter prices 
# until they choose to finish. It should handle invalid inputs gracefully 
# and display the total bill at the end

sum = 0
while True:
    x = input("Enter price (to quit, press 'q'): ")
    if x != 'q':
        try:
            sum += float(x)
            print("Your bill till now is", sum)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Total Bill is", sum, "\nThank you for shopping....")
        break
  

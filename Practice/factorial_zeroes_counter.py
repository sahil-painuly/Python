# Python program that calculates the factorial of a non-negative 
# integer input by the user and counts the number of trailing zeroes in the factorial.

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    

def zeroes(fact):
    list = []
    length = len(str(fact))
 
    for i in range(1,length+1):
        list.append(int(fact%10))
        fact=fact//10
    return list.count(0)

while(True):
    try:
        n = int(input("Enter a non-negative number:"))
        if(n>0):
            factorial = fact(n)

            print("Factorial :",factorial)

            zero =zeroes(factorial)

            print("Number of zeroes in factorial :",zero)
            break
        else:
            print("Invalid input. Please enter a valid non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
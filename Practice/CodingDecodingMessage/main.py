import random as r
import string as s

def coding(message):
    try:
        words = message.split(" ")
        coded_words = []
        for word in words:
            if len(word) >= 3:
                random_word = ''.join(r.choices(s.ascii_lowercase, k=3))
                word = random_word + word[1:] + word[0] + random_word
                coded_words.append(word)
            else:
                word = word[::-1]  
                coded_words.append(word)
        return ' '.join(coded_words)
    except Exception as e:
        print(f"Error occurred: {e}")

def decoding(message):
    try:
        words = message.split(" ")
        decoded_words = []
        for word in words:
            if len(word) >= 3:
                decoded_word = word[3:-3]
                decoded_word = decoded_word[-1] + decoded_word[:-1]
                decoded_words.append(decoded_word)
            else:
                decoded_words.append(word[::-1])
        return " ".join(decoded_words)
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    try:
        user_input = input("Enter the message: ")
        choice = int(input("Press 1 for code for message...\tPress 2 for decode your message.....\n--> "))

        if choice == 1:
            new_msg = coding(user_input)
            print(f"{user_input} is coded as: {new_msg}")
            print("Thank you for using...")
        elif choice == 2:
            new_msg = decoding(user_input)
            print(f"{user_input} is decoded as: {new_msg}")
            print("Thank you for using...")
        else:
            print("Invalid choice! Please enter 1 or 2.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

import random as r
import string as s

def coding(str):
 
 words = str.split(" ")
 codedword = []
 for word in words:
  if len(word)>=3:
   random_word = ''.join(r.choices(s.ascii_lowercase, k=3))
   word = random_word + word[1:] + word[0] + random_word
   codedword.append(word)
  else:
   word = word[::-1]  
   codedword.append(word)
 return ' '.join(codedword)

def decoding(message):
    words = message.split(" ")
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    return " ".join(nwords)

userInput = input("Enter the message : ")
choice = int(input("Press 1 for code for message...\tPress 2 for decode your message.....\n--> "))



if choice == 1:
    newmsg = coding(userInput)
    print(f"{userInput} is coded as \t {newmsg}")
    print("Thankyou for using...")
elif choice == 2:
  newmsg = decoding(userInput)
  print(f"{userInput} is decoded as \t {newmsg}")
  print("Thankyou for using...")


  # ntzahilsntz si a gwboodggwb pzvoybpzv

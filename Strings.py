# string
str = "hello"

# Operations 

# 1.concatenation
str2 = str + "World"
print(str2)

# 2.length
print(len(str2))

# 3.Slicing
print(str2[1:4])
print(str2[:4])
print(str2[1:])

# String functions 
str3 = "I am a coder."

print(str3.count("e")) #counts the occurrence of substr in string
str3.capitalize() #capitalizes 1st char
str3.replace("er", "new") #replaces all occurrences of er with new
print(str3.find("a")) #returns 1st index of 1st occurrence


# Count $ in a given string
username = "$ahilpainuly$$0$"
print("$count :",username.count("$"))

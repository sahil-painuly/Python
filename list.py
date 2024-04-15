list = [1,2,3,4,5] #list are mutable

# List Slicing

print(list[1:4])
print(list[:4])
print(list[1:])

# list methods 

list.append(6)#add in last
list.sort() #asc
list.sort(reverse=True) #desc
list.reverse() #reverse the list 
list.insert(2,45) #insert el acc to indx
list.remove(1) #removes first occurrence of element
list.pop(3) #removes element at idx
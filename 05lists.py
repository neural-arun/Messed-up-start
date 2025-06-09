# LIST & TUPLES
# list= built in datatype
'''list can store elements of different types 
srings are immutable and lists are mutable in python'''
str = "arun"
print(str[1])
#str[1] = "j" ye allowed nhi hai jabki ye cheej list mein allowed hai 
student =["Arun" , 94.13, 20, "prayagraj"]  # indexing yha bhi ki jaati hai 
print(student[1])
student[0] = 88.17
print(student)# ab output mein value change ho jayegi ye cheez sting allow nhi karta hai

#LIST SLICING-similar to string slicing
# list_name[starting_ind:ending_ind]
marks = [9,7,9,8,6,5,3,8,9,4,3,7,6]
print(marks[4:6])#ending idx is not included
print(marks[:6]) # is same as [0:4]
print(marks[1: ])# is same as [1:len(marks)]
print(marks[-3:-1]) # just like string
# indexing 0 se start hoti hai


#LIST METHODS
list = [3,4,5,6,1]
list.append(7)  # adds one value at end of the list
print(list)   # output--[3,4,5,6,1,7]
#SORTING 
list.sort()# ye ascending order mein sorting karta hai agr descending order mein sorting karni hai to neeche dekho ager list mein koi strings hain to vo alphabetical order mein sort hoti hai
print(list)
list.sort(reverse=True)  # ab ye reverse order mein list ko print karke dega 
print(list)
list.reverse()  #ye list ko reverse kar deta hai
print(list)

a = ["kutta",3,67,53,'haathi']
a.insert(4,"pagal")  # ye index 4 pr pagal insert kara dega 
print(a)
a.pop(4) # ye list mein se kisi index se element ko hata deta hai
print(a)















































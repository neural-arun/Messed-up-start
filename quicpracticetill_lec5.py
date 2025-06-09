# practice till lecture 5 
# variable swap without third variable
a = 5
b = 10
print(f"a = " ,10 )
print(f"b = " ,5 )


# type conversion
c = float(input("enter your number :"))
print(int(c))


# string reverser 
s = "python"
print(s[5],s[4],s[3],s[2],s[1],s[0])

# grade calculator
marks = int(input("Enter your marks :"))
if marks >= 90 and marks <=100:
    print("Grade : A")
    
    
    
elif marks >= 80:
    print("Grade : B")
else:
    print("Grade : c")

#list palindrome check 
my_list = [1,2,3,2,1]
v=my_list.copy()
my_list.reverse()
if v == my_list:
    print("List is a palindromic sequence")
    
else:
    print("List is not a palindromic sequence")


# tuple unpacking 
tup = ("alice" , 25 , "NYC" )
name = tup[0]
age = tup[1]
city = tup[2]
print(name,age,city)

#updater dictionary
dicts = {"a" : 1, "b" : 2 }
dicts.update({"c" : 3})

print(dict)

# set operations 
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

# list to dictionary
keys = ["name", "age"]
values = ["bob", 30]
dictionary = dict(zip(keys, values))
print(dictionary)

# case counter
s = "PyThOn"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print(f"Uppercase: {upper}, Lowercase: {lower}")

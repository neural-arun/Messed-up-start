# loops are used to repeat instructions , two types while and for loops 
# "hello world" ko 1 lac baar likhna hai
# while loop - jab tak 
x = 1
while x <= 10  :
    print("ashutosh yadav chutiya hai",x)
    x+=1

y = 34 
while y >= 11 :
    print(y)    
    y -= 1
#q print numbers from 1 - 100
print("QUESTION NO 1")
I = 1
while I <= 100 :
    print(I)
    I += 1
print("printed 1 to 100")
# q 2  print the numbers from 100 to -100
print("QUESTION NO 2")
y = 100
while y >=-100 :
    print(y)
    y += -1 
print("printed 100 to -100")

# q 3 - print the multiplication table of a number n 
print("QUESTION NO 3")
u = int(input("enter number for table :"))
v = 1
while v<=10:
    print(u*v)
    v+=1
# printing powers of 1 - 10 
print("QUESTION NO 4")
power = int(input("Enter power :"))
n = 1
while n<=10 :
    print(n**power)
    n+=1


#q4 print the elements of the following list using a loop 
# [1,4,9,15,25,36,49,64,81,100]
print("QUESTION NUMBER 4")

sqrs = [1,4,9,15,25,36,49,64,81,100] 
idx = 0  # initialisation ---- Mtlab condition ko start kar rhe hain 
while idx<len(sqrs) :
    print(sqrs[idx])
    idx+=2 

print("practicing one more ")
vill_houses = ["Munnilal Yadav" , "Lala Yadav" , "Ramachal Singh" , "Rammilan Yadav" , "Radheshyam Yadav" , "Jogi Yadav" , "Debha yadav" , "Akhilesh Yadav" , "Oma Yadav" , "Sarvesh Yadav" ,"Triloki Yadav" , "Khurmulli Yadav" ,"Manoj Yadav" , "Golu Yadav" , "Rambadh Yadav" , "Jhinku Yadav" ,"Pappu Yadav" , "Kishan Yadav" , "Suman Yadav" ,"Lallu Yadav" , "Vivek Yadav","Chandar Yadav","Vikas Yadav"]
idx = 0 
while idx < len(vill_houses):    # traverse karna Mtlab ek ek element ke upar hm travel  kar rhe hain 
    print(vill_houses[idx])
    idx+=1

#Q- 5 search for a number x in this tuple using loop 
# (1,4,9,16,25,36,49,64,81,100)

































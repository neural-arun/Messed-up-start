# SECTION 2
# challenge 1 (room area calculator)
a = float(input("Enter room length(m) :"))
b = float(input("Enter room width(m) :"))
area = a*b
perimeter = 2*(a+b)
print(f"Area of the square is {area}sq.m,& perimeter of the room is {perimeter}m ")

# challenge 2 
print("can't think how to proceed ?")


# challenge 3 
marks1 = int(input("Enter your marks in English :"))
marks2 = int(input("Enter your marks in social science :"))
marks3 = int(input("Enter your marks in physics :"))
marks4 = int(input("Enter your marks in science :"))
marks5 = int(input("Enter your marks in mathematics :"))

total = marks1+marks2+marks3+marks4+marks5
print("Your total marks is :",total)
percentage = total/5
print("Your total percentage is :",percentage)
print("Feedback")
if percentage > 90:
    print("Excellent")
elif percentage >75 and percentage < 90:
    print("Good")
else:
    print("Need improvement")    

# challenge 4 simple interset calculator
p = float(input("Enter principle :"))
r = float(input("Enter rate :"))
t = float(input("Enter time of interest :"))
interest = (p*r*t)/100
print("Total simple interest is :",interest)




























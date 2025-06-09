# FIRST MEGA PROJECT

name = input("Enter student's name : ")
std = int(input("Enter student's class : "))
roll_no = int(input("Enter student's Roll number : "))
english = int(input("Enter student's  English marks :,"))
mathematics = int(input("Enter student's  mathematics marks :,"))
science = int(input("Enter student's  Science marks :,"))
Hindi = int(input("Enter student's  Hindi marks :,"))
sst = int(input("Enter student's  Social Science marks :,"))
total = english+mathematics+science+Hindi+sst


percentage = total/5

print("="*55)
print("="*15,  "STUDENT DETAILS")
print(f"Student's name :      {name}")
print(f"Student's class :        {std}")
print(f"Student's Roll number :{roll_no}")
print("="*10, "RESULT SUMMARY","="*10)
print(f"Total marks of student is :  {total}")
print(f"Percentage of the student is: {percentage}")
if(percentage>=95):
    print("Grade :","A+")
    print("Feedback : ekdam smart ho be")
elif(percentage>=90):
    print("Grade :","A")
    print("Feedback : jabardast kar rhe ho karte rho")
elif(percentage>=80):
    print("Grade :","B")
    print("Feedback : badhiya hai aur mehnat karo")
elif(percentage>=70):
    print("Grade :","C")
    print("Feedback : potential hai but dheelgavaheen kar rha hai ")
elif(percentage>=60):
    print("Grade :","E")
    print("Feedback : Bahut mehnat karo")
    
else:
    print("Grade :","F")
    print("Feedback : bhai padhai chhod de kuch seekh le ")
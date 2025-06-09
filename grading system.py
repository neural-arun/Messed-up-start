# WAP to take input from students to check their grade 
while True:        # while True use Kiya jata hai program baar run karne mein T capital hai
    marks = int(input("Enter your marks :",))
    if(marks>=90):
        grade= "jalva hai aapka"
      
    elif(marks>=80 and marks<90):
        grade="badhiya hai beta aur mehnat karo"
    elif(marks>=60 and marks<80):
        grade = "accha kar sakta hai"
    elif (marks>=33 and marks<60):
        grade ="backchod lekin thoda kam"
    elif (marks<33):
        grade = ("padhai chod de")
     
    print("Grade of student is :-->",grade)
  
    
      
        
          
            
                
    
    


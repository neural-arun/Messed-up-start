#string is a datatype that store a sequence of characters
#usually double quates ke andar hota hai kyonki single quote sentences mein use hote hain 
#escape sequence characters--for new line:\n ,\t is used for tab space in output
#\n use kiya jata hai new line ke liye in a string in output for example
 
#string1 = "My name is Arun yadav \nI do not know what to do \nI am fucked by NTA three times \nsome of my friends are ready to be fucked again and \t some are gonna fucked by some other governmeint exams"
#print(string1)
# yha par jaha jaha \n hai vha se output mein nayi line shuru hogi
 
# basic operations #1 concatenation
str1 = "Arun" 
str2 = "Yadav"
concatenatedstr = str1 +" "+ str2
print(concatenatedstr)     #output = Arun Yadav

#basic opertion2 length of a string
print(len(str1))
print(len(str2))
 #print lagana nhi bhoolna hai
 
   # indexing operation
   #index characters ko positions de deta hai   (arun_yadav)
   #index help karte hain to access characters (012345678)
# kisi character ko access karne ke liye hm [ ] brackets ka use karte hain for example 
str3 = "Arun yadav" 
charac = str3[2] 
print(charac) # output :u 
#accessing parts of strings
#SLICING
print(str3[5:10])
print(str3[5: ])
print(str3[5:len(str3)])  # ye teeno print same hain 

print(str3[:3]) # ismein 3 include nhi hota hai
print(str3[:4]) # ye 4-1 index tak print karega  
    
#slicing negative index    arun yadav     
#                                          -10-9-8-7-6-5-4-3-2-1 
#STRING FUNCTIONS

str4 = "ashutosh yadav ji chutiye hain"
print(str4.endswith("hai"))            # true or false return karta hai                            
print(str4.capitalize())  #first letter ko capitalise kar deta hai
print(str4.replace("chutiye","smart")) # change kar deta hai
print(str4.find("yadav")) # jha par bhi ye character / word first time exist karta hai uska index aa jata hai
print(str4.count("a"))  #koi substring kitne baar exist karta hai
# aur bhi bahut saare functions hote hain                                                  
                                                              
                                                                     
                                                                            
                                                                                   
                                                                                          
                                                                                                 
                                                                                                        
                                                                                                               
                                                                                                                      
                                                                                                                             
                                                                                                                                           
        
         
          
           
            
             
              
               
                
                 
                   
    
   
    
     
      
       
        
         
          
           
            
              
 
 
 
 
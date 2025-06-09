info = { 
"name" : "Arun yadav",
"class" : "learner",
"subjects" : ("python" ,"AI","ML"),
"age" : 20 ,
"is_adult " : True ,}

print(type(info)) # output : class : dict aayegi 
 # agar key ki values ko access karna hua to 
print(info["class"])
print(info["age"]) 

info["class"] = "unknown" # yha key ki values change aise ki jaati hai 
info["father_name"] = "Subash yadav"  # same aise hi nayi key alue create ki jati hai  
print(info)
null_dict = { }   # pahle null dictionary banao phir usmein kuch add bhi kar sakte ho 
null_dict["name"] = "arun yadav"
print(null_dict)
# NESTED dictionary - dictionary ke andar dictionary
student = { "name" : "Arun Yadav",
"class" : "unknown",
"subjects_marks" : { "phy" : 98 ,
"che" : 97 ,
"math" : 88.9},
"age" : 20 , }
print(student)
print(student["subjects_marks"]["math"])  # ye dict ke andar dict ki value nikalne ke liye 
a = student.keys()
print(a)  # ye sabhi key values ko deta hai , nested vali keys ko  nahi deta hai
print(list(a))  # ye sabhi key values ko list ke roop mein deta hai 
print(len(student)) # ye total kitni keys hain ye batata hai 
b = student.values() # ye saari values ko return karta hai
print(b)
print(list(b)) # values ko list ke roop mein return karva diya 
c = student.items()
print(c)  # returns all (key, value pairs) as tuples    
print(list(c)) # list ke tuple mein key value pairs ko return karega 
d = student.get("name")
print(d)
print(student["name"])  # ye dono cheezen ek hi kaam kar rhi hain hain lekin ek difference hai 
print(student.get("name2"))  # ye hame none return karke dega lekin ager 
###print(student["name2"])  # kiya to ye hame error de dega  
student.update({"city" : "azamgarh"})
print(student)   # ye method dictionary ke andar nayi key value pairs ko add kar deta hai
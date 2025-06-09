# DICTIONARIES AND SETS 
person_info = { "name" : "alice" ,
"age" : 30 ,
"location" : "new york"          # isi ko dictionary bolte hain
}                         
print(person_info)
print(person_info["name"])   # kisi key ke values ko paane ke liye use Kiya jaata hai 
person_info["age"] = 35   # kisi key ki values change karne ke liye kiya jata hai
print(person_info)
keys = person_info.keys()  # saare keys ko access kiya jata hai
print(keys)
values = person_info.values()  # saare values ko access kiya jata hai 
print(values)  
entries = person_info.items()   # saare key and values ko ek sath paane ke liye kiya jaata hai 
print(entries)
for key,value in  person_info.items():
    print(key,value)       # aise sare keys values ko alag alag paane ke liye kiya jata hai
updates = {"occupation":"engineering"}
person_info.update(updates)
print(person_info)    # aise keys and values ko update karne ke liye kiya jaata hai 
name = person_info.pop("name")   # ise kise key value pairs hata dia jata hai
print(person_info)
squares = {x : x**2 for x in range(6)}
print(squares)
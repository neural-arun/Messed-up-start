# set is a collection of unordered items  set is mutable but elements are immutable 
# each element in the set must be unique and immutable . duplicate values ko sets ignore kar deta hai ok 
children = {"arun yadav","Sarita yadav","uday pratap yadav","arun yadav","arun yadav"}
print(children)  # arun yadav ,Sarita yadav ,uday pratap yadav 
print(type(children)) # class : set
print(len(children))  # 3 (total number of items aayega )

sons = {}  # empty set kaise banaye but agar aise karenge to empty dict bn gayi hai
print(type(sons))
# empty set : syntax
daughters = set()
print(type(daughters))
# set methods
daughters.add("Sarita yadav")
daughters.add("geeta yadav")
daughters.add((1,2,3,4,5,4,4,4)) # sets mein tuple add kar sakte hain
#daughters.add([1,2,3,4,5,6,7])  # yha se error aata hai kyonki list ko add nahi kar sakte hain  
# jo bhi value immutable hoti hain unko add kar sakte hain --- hashable value

# jo value baad mein jaker change ho jaye unko unhashable value bolte hain 
daughters.pop()  # removes a random value  ekdum random hai ye  
print(daughters)
daughters.remove("Sarita yadav")
print(daughters)
print(len(daughters))  # 2
daughters.clear()  # ye set ko empty kar deta hai
print(len(daughters))  # 0
print(daughters)
# UNION & INTERSECTION OF SETS 
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
a = set1.union(set2)
b = set1.intersection(set2)
print(a)
print(b)



















# sets in python 
# unordered collection featuring unique items. they highlight their utility in scenarios demanding a distinct aggregation of elements such as removing duplicates and performing set arithmetic and comparisons.
primes = {2,3,5,7,11}
mixed_set = set(["apple",42,(5,6)]) # square brackets lagana bahut jaroori hai 
print(mixed_set)
print(primes)
# adding elements 
primes.add(13)
print(primes)
mixed_set.add("mango")
print(mixed_set)
# set operations 
odds = {1,3,5,7,9}
union_set = primes.union(odds)
print(union_set)
common_elements = primes.intersection(odds)
print(common_elements)
diff_set = primes.difference(odds)
print(diff_set)
sym_diff = primes.symmetric_difference(odds)
print(sym_diff)
# FROZEN SETS -- frozen sets are immutable versions of regular sets 
frozen_primes = frozenset(primes)
print(frozen_primes)

# combining set and dictionary 
# yha par dictionary ke andar set hai 

multiclass_students = {"math": {"alice","bob"},
               "biology" : {"bob","catherine"},
}
multiclass_students["physics"] = {"alice"}
print(multiclass_students)



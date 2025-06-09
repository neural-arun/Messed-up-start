#WAP to check if a list contains a palindrome of elements ,use copy() method
list1 = [1,2,3,2,1]

list_copied = list1.copy()

list1.reverse()

if(list1==list_copied):
    print("list 1 is is a palindrome ")

else:
    print("no list is palindrome ")















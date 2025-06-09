#WAP to check if a DNA sequence can be cut by R.E. or not.??
print("="*10,"CHECKING PALINDROMIC DNA","="*10)
seq1 = ["A","T","T","G","G","C"]
seq2 = ["C","G","G","T","T","A"]

seq = seq1.copy()  
seq1.reverse()  # agr keval yhi karoge to none ayega copy ke sath reverse karna hota hai
if(seq1==seq2):
    print("This DNA sequence can be cut by restriction endonuclease")
    
else:
    print("This DNA sequence can not be cut by restriction endonuclease")



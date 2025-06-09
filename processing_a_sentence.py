# processing a sentence 
print("="*10, "PROCESSING A SENTENCE " ,"="*10)
sentence = input("Enter sentence tou want to check :").lower()
# counting chraracters in a string
sentence1 = len(sentence)
print("Total number of characters in your sentence are :",sentence1)
# counting vowels in a sentence
vowel_a = sentence.count("a")
vowel_u = sentence.count("u")
vowel_o = sentence.count("o")
vowel_i = sentence.count("i")
vowel_e = sentence.count("e")
total_vowel = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u
print("Total number of vowels in your sentence are :",total_vowel)
# creating a list of all words using split()

list_of_words = sentence.split()
print(list_of_words)
# reversing the words in a sentence
reversed_sentence = sentence[::-1]
print("Reversed sentence is :",reversed_sentence)
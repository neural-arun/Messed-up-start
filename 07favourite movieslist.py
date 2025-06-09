# WAP to ask the user to enter their name and 3 favourite movies, and store them in a list

# Taking user's name
name = input("Enter your name: ")
print("Welcome,", name)

# Taking 3 favourite movies and storing them directly in a list
movies = [
    input("Enter your favourite movie 1: "),
    input("Enter your favourite movie 2: "),
    input("Enter your favourite movie 3: ")
]              # list mein bhi input directly liya ja  sakta hai 

# Printing the result in a clean format
print(f"Favourite movies of {name} are: {', '.join(movies)}")    #  ', '.join(movies)  ye function string ko join karta hai comma lga ke 
# Lesson 2- DataTypes & String_Manipulation
'''
#String (str)
# String must always be in quotation!
name = "Muaz"
name = input("Please enter your name")
#Integer (int)
age = 16
age = int(input("Please enter your age"))

#Float (float)
pi_value = 3.14
pi_value = float(input("What is the value of pi?"))

#Boolean (bool)
# For bool you use == instead of bool(input())
age_is_16 = True
age_is_16 = False
answer = input("You are 16? True or False?")
age_is_16 = (answer == "True")

#None (NoneType)
test_results = None
'''

#String Manipulation

#Case modification

#Upper
print("hello".upper())
favgame = input("Enter your favourite game").upper()
print(favgame)

#Lower
print("hello".lower())
favdrink = input("Enter your favourite drink").lower()
print(favdrink)

#Title
print("hello".title())
name = input("Enter your name").title()
print(name)

#capitalize
print("hello world!".capitalize())

#swapcase
print("pYTHON".swapcase())

#Cleaning and trimming

#strip
print(" python ".strip())

#lstrip
print(" python ".lstrip())

#rstrip
print(" python ".rstrip())

#removeprefix
print("https://GitHub.com".removeprefix("https://"))

#removesuffix
print("DataTypes_and_StringManipulation.py".removesuffix(".py"))

#Splitting and Joining

#split
print("Zelda-Genshin-Honkai".split("-"))

#splitlines
print("Zelda\nGenshin\n".splitlines())

#join
print(" ".join(["Genshin", "Impact"]))

#Search and Inspection
print("Honkai" in "Honkai impact 3rd")

#Find
print("Honkai".find("a"))

#Count
print("Honkai Star Rail".count("a"))

#Startswith
print("SwordArtOnline".startswith("S"))

#Endswith
print("SwordArtOnline".endswith("e"))

#Content Verification
#isalnum
print("HonkaiImpact3rd".isalnum())

#isalpha
print("Zelda".isalpha())

#isdigit
print("5103".isdigit())

#isspace
print(" ".isspace())

#Substrings and slicing

#Slicing
print("Zelda"[0:2])

#Reversing
print("live"[::-1])

#Advanced Alterations
print("Zelda".replace("a", "o"))

#Partition
print("genshin-honkai-zelda".partition("-"))

#Formatting and Padding

#F-strings
name = "Muaz"
f"Hi, {name}"

#zfill
"16".zfill(5)

#ljust/ rjust
"Mario".ljust(5, "-")
"Link".rjust(5, "-")

#Center
"Muaz".center(6, "-")
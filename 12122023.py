#Get a string from user and replace the last char by ing
#if the string already endswith 'ing' then print as it is
 
#shopping - shopping
#cakes - cakeing

s = input("Enter a word: ")

# if not s.endswith('ing'):
#     s = s.replace(s[-1], '') + "ing"


#if the input string is uppercase then convert to lower
#MANASA - manasa
#if the input is lower => upper, if it is capitalized then convert the
#remaining char's into upper case.
#Manasa => mANASA
#input is combination of upper or lower mAnaSa => invalid input

if s.islower():
    s= s.upper()
elif s.isupper():
    s= s.lower()
elif s.istitle():
    s = s[0].lower() + s[1:].upper()

else:
    print("Invalid Input")

print(s)

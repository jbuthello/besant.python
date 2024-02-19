#find if the string ends with vowel

b= input("Enter a sentence: ")
a= b.lower()
i= a.length()-1
if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
    print("First letter is vowel")
else:
    print("does not start from vowel")

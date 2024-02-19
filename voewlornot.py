#find if the first letter of string is vowel or not

b= input("Enter a sentence: ")
a= b.lower()
if(a[0]=='a' or a[0]=='e' or a[0]=='i' or a[0]=='o' or a[0]=='u'):
    print("First letter is vowel")
else:
    print("does not start from vowel")

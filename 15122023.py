#find the square value of given number
'''
#find factorial if a number
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print("factorial value is: ",f)
n = int(input("enter the number"))
fact(n)


 
#get addition of two numbers
add=lambda a,b:a+b
b=int(input("Enter the first number"))
c=int(input("Enter the second number:"))
print(add(b,c))


#find the given number is even or odd
res = lambda n : "even" if(n%2==0) else "odd"
print(res(4))
 

'''
#find the max of two numbers
'''
max=lambda a,b: print(a) if a>b else print(b)
a=int(input("ENter first number: "))
b=int(input("Enter second number: "))
max(a,b)
'''

#find the given string startswith 'a' or not

# firsta=lambda s: True if s[0] in 'aA' else False
# s=input("Enter a string")
# print(firsta(s))
#find the given number is +ve or negative
# range=lambda m: True if not 0 and m>1 else False
# m=input("Enter a number ")
# print(range)

#find the max of three numbers

'''
if(a>b and a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)
 
 
res = lambda a,b,c : a if(a>b and a>c) else (b if(b>c) else c)
 
print(res(2,3,4))
 
'''
#Find the given number is bewtween 1 to 10 or above 10 or below 1
range1=lambda n: "Between 1 to 10" if 1<= n<11 else ("above 10" if n>10 else "below 1") 
n=int(input("enter number: "))
print(range1(n))

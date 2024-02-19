#Find the grade of the student(100 to 90-A,90 to 80 - B, 80 to 70 - C, below 70 no grade)
a=float(input("Enter student's Paecentage "))

if(a>90 and a<=100):
    print("A Grade")
elif(a>80 and a<=90):
    print("B Grade")
elif(a>70 and a<=80):
    print("C Grade")
elif(a<70):
    print("No Grade")

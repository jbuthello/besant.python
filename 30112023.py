# find leap years from 2000 to 2020
year = 2000

while year <= 2020:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
    year += 1

'''
Data types:-
 
1. List - Collection of different data []
(Mutable-add,update and delete elements inside a list)
 
2. Tuple - Collection of different data  ()
(Immutable - can't change elements)
 
3. Set - It has no index {}
 
4. String - Collection of diff char's - either '' or ""
 
5. Dictionary - Key and value pair of data.
(Mutable-add,update and delete elements inside a dict)
{}
 
6. Numbers(int,float) - Immutable
 
'''
#l = [1,2,3,4]
 
  #  0 1 2 3
'''
for i in l:
    print(i)
i=0
while(i<len(l)):
    print(l[i])
    i=i+1
'''

# [6:50 PM] Vani (Guest)
# Methods:-

# l = []
# size = int(input("enter the size"))
# for i in range(size):
#     ele = int(input("enter the elements"))
#     l.append(ele)
# print(l)
# l = [10,2,3,4,6]
# l.sort()
#l.reverse()
# print(l)
#l1 = [4,5]
#l1.remove(5)
#print(l1)
#l1.pop(1)
#print(l1)
 
#l.insert(1,11)
#print(l)
#print(l.index(2))
#l.extend(l1)
#print(l,l1)
#print("count is: ",l.count(4))
#l1 = l.copy()
# print(dir(l))
#l.clear()
#print(l1)


l = ['apple','mango','banana','orange']
#print the elements startswith vowel
list = ['apple','mango','banana','orange']
for i in list:

    if i[0].upper() in ["A", "E", "I", "O", "U"]:
        print(i)
    

# #print the length of the list without using len()




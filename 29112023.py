
'''
Print the following pattern,
1.
*
**
***
'''
n = 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()

'''
2.
    *
  * * *
    *
 '''
n = 3
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()

'''
3.
***
**
* 
'''
n = 4
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print()

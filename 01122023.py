# index of the elements in the list
# l = [1,2,3,1,4,5,6,3,6,7,9,10,2,11]
# #    0 1 2 0 4 5 6 2 6 9 10 11 1 13
# for i in l:
#     print(l.index(i))


'''
slicing - separating elements
l[s:e] - start to end-1
l[:e] - 0 to end-1
l[s:] - start to end
l[:] - return all the elements
l[::2] - step count
'''
l = [11,12,13,14,15,16,17,18,19]
   # 0  1  2  3  4   5  6  7  8
# print(l[1::2])
# print(l[1:6])
# print(l[:])
# print(l[:7])
# print(l[3:])



print(l[:-3])
print(l[-8:-2])
print(l[-6:])
print(l[::-1])

'''
 [12, 13, 14, 15, 16]
[11, 12, 13, 14, 15, 16, 17, 18, 19]
[11, 12, 13, 14, 15, 16, 17]
[14, 15, 16, 17, 18, 19]
'''
 
 
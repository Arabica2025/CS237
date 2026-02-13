import random

deck = [1,2,3,4,5,6,7,8,9,10,11]
for i in range(len(deck)):
    print(f"index{i} reached. element in index{i}: deck[{i}] = {deck[i]}")
    
print(len(deck))

# r = [0,0,2,8,1]
# b = [4,3,2,1,0]


# r_non_leading_zero_index = 0
# for i in range(len(r)):
#     if r[i]== 0:
#         r_non_leading_zero_index+=1
#         #print("0")
#     else:
#         #index = i
#         # r_non_leading_zero_index +=1
#         break
# print(f"the number of zero is: {r_non_leading_zero_index}")
# print(f"index: {i}")

# print(r)
# print(b)
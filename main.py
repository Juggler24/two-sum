import re
#nums = [2,7,11,15], target = 9

num_list = []
target = 0
user_input = input("Input: ")
user_input = user_input.split("[")[1]
flag = False

i = 0
temp = user_input.split(",")
while i < len(temp):
    num_list.append(int(re.sub(r'[^0-9]', '', temp[i])))
    i += 1
target = num_list[len(num_list)-1]
num_list.pop()

for i in range(len(num_list)-1):
    for j in range(i+1, len(num_list)):
        if num_list[i] + num_list[j] == target:
            flag = True
        if flag == True:
            break
    if flag == True:
        break

print("Output: ["+str(i) + "," + str(j)+"]")

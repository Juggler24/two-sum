from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                flag = True
            if flag == True:
                break
        if flag == True:
            break
    
    temp = []
    temp.append(i)
    temp.append(j)
    return temp
    

#nums = [2,7,11,15]
#target = 9

# https://leetcode.com/problems/two-sum/

def find(nums, target):
    item = dict()
    array = []
    for i in range(len(nums)):
        print(item)
        if target-nums[i] in item:
            print(nums[i])
            array.extend([item[target-nums[i]], i]) 
            break
        item[nums[i]] = i
    return array

print(find([3,2,4], 6))
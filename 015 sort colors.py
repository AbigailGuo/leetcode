# https://leetcode.com/problems/sort-colors/
def sortColors(nums):
    start = 0
    end = len(nums)-1
    index = 0
    while index<=end:
        if nums[index]==0:
            swap = nums[index]
            nums[index] = nums[start]
            nums[start]=swap
            start += 1
            index += 1
        elif nums[index]==2:
            swap = nums[index]
            nums[index] = nums[end]
            nums[end] =  swap
            end -= 1
        
            
        else:
            index += 1
        print(index, start, end, nums)
    print(nums)

sortColors([2,0,2,1,1,0])
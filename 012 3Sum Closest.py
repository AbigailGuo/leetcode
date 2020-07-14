# https://leetcode.com/problems/3sum-closest/
def three_sum_closest(nums, target):
    if len(nums)<3:
        return 0
    if len(nums) == 3:
        return sum(nums)
    nums.sort()
    fix = 0
    gap = float('inf')
    small_sum = 0
    while fix<=len(nums)-3:
        left = fix+1
        right = len(nums)-1
        
        while left<right:
            if nums[fix]+nums[left]+nums[right]==target:
                # print(nums[fix],nums[left],nums[right])
                return target
            print("fix, left, right ", fix, left, right)
            if abs(nums[fix]+nums[left]+nums[right]-target)<gap:
                small_sum = nums[fix]+nums[left]+nums[right]
                gap = abs(nums[fix]+nums[left]+nums[right]-target)
            print("gap ", gap, small_sum)
            if nums[fix]+nums[left]+nums[right]<target:
                left += 1
                
                
            print("+left", left, right)
            if nums[fix]+nums[left]+nums[right]>target:
                right -= 1
               
                
            print("-right", left, right)
            
        while fix<len(nums)-2 and nums[fix+1]==nums[fix]:
            fix += 1
        fix += 1
    return small_sum

print(three_sum_closest([-1,0,1,1,55]
,3))
        


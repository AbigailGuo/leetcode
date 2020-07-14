# https://www.lintcode.com/problem/3sum-smaller/description
def three_sum_closest(nums, target):
    if len(nums)<3:
        return 0
    if len(nums) == 3:
        if sum(nums)>=target:
            return 0
        else:
            return 1
    nums.sort()
    fix = 0
    count = 0
    while fix<=len(nums)-3:
        left = fix+1
        right = len(nums)-1
        while left<right:   
            
            if left<right and nums[fix]+nums[left]+nums[right]>=target:
                    right -= 1
            else:
            # print(fix, left, right)
            
                count += right-left
            
                left += 1
        fix += 1
    return count
            
                
print(three_sum_closest([-2,0,1,3],2))
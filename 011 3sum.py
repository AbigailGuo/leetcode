# https://leetcode.com/problems/3sum/
def three_nums(nums):
    if len(nums)==0:
        return []
    result = []
    # 排序
    nums.sort()
    print(nums)
    if len(nums)<3:
        return []
    if nums[0]>0:
        return []
    if nums[len(nums)-1]<0:
        return []
    if nums[0]==0 and nums[len(nums)-1]==0:
        return [[0, 0 ,0]]
    fix = 0
    while nums[fix]<=0 and fix<=len(nums)-3:
        print("fix", fix)
        new_array = [nums[fix]]
        find = False
        left = fix +1
        target = -nums[fix]
        right = len(nums)-1
        while left<right and left<len(nums)-1:
            if nums[left]+nums[right]<target:
                while left<right and nums[left+1]==nums[left]:
                    left += 1
                left += 1
                print("left", left)
            elif nums[left]+nums[right]>target:
                while left<right and nums[right-1]==nums[right]:
                    right -= 1
                right -=1
                print("right", right)
            else:
                new_array.extend([nums[left], nums[right]])
                result.append(new_array)  
                new_array = [nums[fix]]
                print("left, right", left, right)
                while left<right and nums[left+1]==nums[left]:
                    left += 1
                left += 1
                while left <right and nums[right-1]==nums[right]:
                    right -= 1
                right -=1
        
        while fix+1<=len(nums)-3 and nums[fix+1] == nums[fix]:
            fix += 1
        fix += 1
    return result

print(three_nums([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
        





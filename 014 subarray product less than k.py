# https://leetcode.com/problems/subarray-product-less-than-k/
def numSubarrayProductLessThanK(nums, k):
    if min(nums)>=k:
        return 0
    count = 0
    left = 0
    right = 0
    product = 1
    while left<=right and right<=len(nums)-1:
        
        
        product *= nums[right]
        right += 1
        
        while left<right and product>=k:
            product /= nums[left]
            left += 1
        # print(left, right)
        count += right-left
    
            
        
    return count

print(numSubarrayProductLessThanK([10, 5, 2, 6, 1], 100))


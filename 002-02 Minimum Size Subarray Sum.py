# https://leetcode.com/problems/minimum-size-subarray-sum/
def minSubArrayLen( s, nums):
    if sum(nums)<s:
        return 0
    sums = [0]
    for i in range(1, len(nums)+1):
        sums.append(nums[i-1]+sums[i-1])
    print(sums)
    def find(left, right, key):
        while left<=right:
            mid = int((left+right)/2)
            if(sums[mid]>=key):
                right=mid-1
            else:
                left=mid+1
        return left
    min_length = len(nums)
    for i in range(len(nums)):
        right = find(i+1, len(sums)-1, sums[i]+s)
        if right==len(nums)+1: break
        print(i, right)
        min_length = min(right-i, min_length)
    print(min_length)
    return min_length

minSubArrayLen(7,
[2,3,1,2,4,3])
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def read_array(nums):
    # if len(nums) == 0:
    #     return 0
    # if len(nums) == 1:
    #     return 1 
    # sum_array = 1
    # now = nums[0]
    # for i in range(1, len(nums)):
    #     if nums[i] != now:
    #         now = nums[i]
    #         sum_array += 1
    # return sum_array

    if len(nums) == 0 or len(nums)==1:
        return nums
    left = 0
    now = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != now:
            left += 1
            now = nums[i]
            nums[left] = now
    left += 1
    print(nums)
    return left

print(read_array([1, 1, 2]))


# if len(nums) == 0 or len(nums)==1:
#             return nums
#         left = 0
#         now = nums[0]

#         for i in range(1, len(nums)):
#             if nums[i] != now:
#                 left += 1
#                 now = nums[i]
#                 nums[left] = now
#         left += 1
#         while len(nums)>left:
#             del nums[left]
#         return nums
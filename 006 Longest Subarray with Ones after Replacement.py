def max_one(s, k):
    right = 0
    left = 0
    one_number = 0
    max_length = 0
    for right in range(len(s)):
        if s[right]==1:
            one_number += 1
        # print(max_repeat, k, right, left)
        # print(char_set)
        while one_number+k<right-left+1:
            if s[left] == 1:
                one_number -= 1
            left += 1          
        max_length = max(max_length, right - left+1)
    return max_length

a = [1, 0, 0, 1, 0, 1, 0, 1 ] 
length_k = 2 
print(max_one(a, length_k)) 
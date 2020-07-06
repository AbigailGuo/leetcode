
def max_replace(s, k):
    right = 0
    left = 0
    max_repeat = 0
    char_set = dict()
    max_length = 0
    for right in range(len(s)):
        if s[right] in char_set:
            char_set[s[right]] += 1
        else:
            char_set[s[right]] = 1
        if max_repeat<char_set[s[right]]:
            max_repeat = char_set[s[right]]
        # print(max_repeat, k, right, left)
        # print(char_set)
        while max_repeat+k<right-left+1:
            
            char_set[s[left]] -= 1
            left += 1
            max_repeat = max(char_set.values())
            
        max_length = max(max_length, right - left+1)
    return max_length


# print(max_replace("aBaac", 1))
# T = int(input())
# for time in range(T):
#     para = list(map(int, input().split()))
#     n = para[0]
#     k = para[1]
#     input_s = input()
#     print(max_replace(input_s, k))

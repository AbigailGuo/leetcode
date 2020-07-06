# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    char_set = dict()
    max_length = 0
    while right<len(s):
        if s[right] not in char_set:
            char_set[s[right]] = right
            right += 1
        else:
            left = max(left, char_set[s[right]]+1)
            char_set[s[right]] = right
            right += 1
        print(char_set)
        print(left, right)
        max_length = max(right-left, max_length)
    return max_length

print(lengthOfLongestSubstring("abba"))
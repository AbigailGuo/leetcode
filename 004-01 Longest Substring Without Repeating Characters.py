# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    left = 0
    right = 0
    char_set = set()
    max_length = 0
    while right<len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            right += 1
        
        else:
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            right += 1
        max_length = max(right-left, max_length)
    return max_length

print(lengthOfLongestSubstring("pwwkew"))
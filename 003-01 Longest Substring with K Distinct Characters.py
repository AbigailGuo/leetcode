def lengthOfLongestSubstringKDistinct(s, k):
    if k==0:
        return 0
    if len(s)<=k:
        return len(s)
    print(len(s))
    left = 0
    right = 0
    max_length = 0
    array = dict()
    while right<len(s):
        if s[right] in array:
            array[s[right]] += 1
        else:
            array[s[right]] = 1
        print(right, left)
        
        print("max length", max_length)
        right += 1
        while len(array)>k:
            print(len(array), array)
            array[s[left]] -= 1
            if array[s[left]]==0:
                del array[s[left]] 
            left += 1
        max_length = max(right-left, max_length)
    return max_length

# print(lengthOfLongestSubstringKDistinct("nfhiexxjrtvpfhkrxcutexxcodfioburrtjefrgwrnqtyzelvtpvwdvvpsbudwtiryqzzy", 25))
print(lengthOfLongestSubstringKDistinct("eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh", 16))
            
             
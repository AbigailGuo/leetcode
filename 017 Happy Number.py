# https://leetcode.com/problems/happy-number/
def isHappy(n):
    def sumResult(n):
        result = 0
        while n>=1:
            result += pow(n%10, 2)
            n = n//10
        return result
    new_number = n
    linked_list = []
    index_list = []
    index = 0
    while 1:
        if new_number==1:
            return True
        new_number = sumResult(new_number)
        if new_number in linked_list:
            return False
        linked_list.append(new_number)
        index_list.append(index)
        
        index += 1







print(isHappy(19))
        

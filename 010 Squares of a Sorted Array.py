# https://leetcode.com/problems/squares-of-a-sorted-array/


def sorted_square(A):
    right = 0
    for i in range(1, len(A)):
        if A[i-1]<0 and A[i]>=0:
            right = i
            break
    print(right)
    if A[0]>=0:
        right = 0
    if A[len(A)-1]<0:
        right = len(A)-1
    print(right)
    left = right-1
    result = []
    while left>=0 and right<= len(A)-1:
        if abs(A[left])>abs(A[right]):
            result.append(A[right]*A[right])
            right += 1
        else:
            result.append(A[left]*A[left])
            left -= 1
    while left>=0:
        result.append(A[left]*A[left])
        left -= 1
    while right<= len(A)-1:
        result.append(A[right]*A[right])
        right += 1
    return result

print(sorted_square([-7,-3,2,3,11]))


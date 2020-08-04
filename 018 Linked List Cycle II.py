# https://leetcode.com/problems/linked-list-cycle-ii/
def detectCycle(head):
    # 判断是否成环
    slow = fast = head
    loop = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop = True
            break
    if not loop:
        return None
    fast = head 
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast
    

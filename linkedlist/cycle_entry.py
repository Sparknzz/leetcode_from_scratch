
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, right=None):
        self.val = val
        self.next = right
    
# 找到入口点  这个需要一些数学推导
def check_cycle(root):

    slow = root
    fast = root

    while fast.next is not None and  fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            
            # 找到相交点之后 让满指针继续走  定义一个新指针 从头走 当两个值相等时 就是入口
            temp = root

            while temp.next is not None and slow.next is not None:
                temp = temp.next
                slow = slow.next

                if temp == slow:
                    return temp 

            # return True

    return False


r1 = ListNode(1)
r2 = ListNode(2)
r3 = ListNode(3)
r4 = ListNode(4)
r5 = ListNode(5)
r6 = ListNode(6)

r1.next = r2
r2.next = r3
r3.next = r4
r4.next = r5
r5.next = r6
r6.next = r3
# 定义了一个有环的列表

print(check_cycle(r1))
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def addTwoNumbres(self):

        num1 = 0
        num2 = 0
        res = 0
        res_list = []

        if (self.l1 == []) or (self.l2 == []):
            print("One or more lists are empty, Please enter a num lists between [1-100] only")
        else:
            for numL1 in reversed(self.l1):
                if numL1 >= 0 or numL1 <= 100:
                    num1 = num1 * 10 + numL1
                else:
                    print("The digit are not in the corrct range.")
            for numL2 in reversed(self.l2):
                if numL2 >= 0 or numL2 <= 100:
                    num2 = num2 * 10 + numL2
                else:
                    print("The digit are not in the corrct range")

            res = num1 + num2
            revers_num = str(res)[::-1]

            for digit in revers_num:
                res_list.append(digit)

            return res_list



print("----------------------------------------------")
Solution1 = Solution([2, 4, 3], [5, 6, 4])
print(Solution1.addTwoNumbres())
print("----------------------------------------------")
Solution2 = Solution([0], [0])
print(Solution2.addTwoNumbres())
print("----------------------------------------------")
Solution3 = Solution([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
print(Solution3.addTwoNumbres())
print("----------------------------------------------")
Solution4 = Solution([0,7,5], [9,6])
print(Solution4.addTwoNumbres())
print("----------------------------------------------")


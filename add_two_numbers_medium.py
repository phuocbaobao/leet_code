# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_to_list_node(self, lst):
        if len(lst) == 1:
            return ListNode(lst[0])
        return ListNode(lst[0], self.list_to_list_node(lst[1:]))

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = {"val": 2, "next": {"val": 4, "next": {"val": 3, "next": None}}}
        l2 = {"val": 5, "next": {"val": 6, "next": {"val": 4, "next": None}}}

        r1 = []
        r2 = []

        while True:
            if l1["next"]:
                r1.append(l1["val"])
                l1 = l1["next"]

            if l2["next"]:
                r2.append(l2["val"])
                l2 = l2["next"]

            if not l1["next"] and not l2["next"]:
                r1.append(l1["val"])
                r2.append(l2["val"])
                break

        r1 = ''.join(str(r) for r in reversed(r1))
        r2 = ''.join(str(r) for r in reversed(r2))

        result = int(r1) + int(r2)
        reserved_result = reversed(str(result))

        reserved_result = [int(r) for r in reserved_result]

        return self.list_to_list_node(reserved_result)


if __name__ == "__main__":
    solution = Solution()
    print(solution.add_two_numbers([2, 4, 3], [5, 6, 4]))
    print(solution.add_two_numbers([0], [0]))
    print(solution.add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))

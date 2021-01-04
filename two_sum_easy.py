from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            leftover = target - nums[i]

            if leftover in nums and nums.index(leftover) != i:
                return [i, nums.index(leftover)]
            continue


if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum(nums=[2, 7, 11, 15], target=9))
    print(solution.two_sum(nums=[3, 2, 4], target=6))
    print(solution.two_sum(nums=[3, 3], target=6))

from typing import List


class Solution:
    def sum_arr(self, arr: List[int]):
        median_index = int((len(arr) - 1) / 2)

        if len(arr) % 2 == 0:
            return (arr[median_index] + arr[median_index + 1]) / 2
        return arr[median_index]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not len(nums1):
            return self.sum_arr(nums2)

        if not len(nums2):
            return self.sum_arr(nums1)

        if not len(nums2) and not len(nums1):
            return 0

        merged_arr = sorted(nums1 + nums2)
        return self.sum_arr(merged_arr)


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
    print(solution.findMedianSortedArrays([0, 0], [0, 0]))

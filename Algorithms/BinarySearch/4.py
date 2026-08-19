from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_iter = iter(nums1)
        nums2_iter = iter(nums2)

        it1 = next(nums1_iter, "end")
        it2 = next(nums2_iter, "end")

        merge_list = []

        while True:
            if it1 == "end" and it2 != "end":
                merge_list.append(it2)
                it2 = next(nums2_iter, "end")
            elif it2 == "end" and it1 != "end":
                merge_list.append(it1)
                it1 = next(nums1_iter, "end")
            elif it1 == it2 == "end":
                break
            elif it1 != "end" and it2 != "end":
                if it1 <= it2:
                    merge_list.append(it1)
                    it1 = next(nums1_iter, "end")
                else:
                    merge_list.append(it2)
                    it2 = next(nums2_iter, "end")
        n = len(merge_list)
        if n == 0:
            return 0 / 1
        elif n % 2 == 1:
            return merge_list[n // 2] / 1.0
        else:
            return (merge_list[n // 2 - 1] + merge_list[n // 2]) / 2
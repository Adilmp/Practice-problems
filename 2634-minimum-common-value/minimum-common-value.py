class Solution(object):
    def getCommon(self, nums1, nums2):
        seen = set(nums1)  # store all nums1 in a set
        for num in nums2:  # since nums2 is sorted, you'll find the smallest match first
            if num in seen:
                return num
        return -1
#O(n+m) = Time complexity
#O(n) = space complexity converting list into set
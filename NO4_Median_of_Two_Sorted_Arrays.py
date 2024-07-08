class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        sorted_nums=sorted(nums1+nums2)
        if len(sorted_nums)%2==0:
            return (sorted_nums[len(sorted_nums)//2]+sorted_nums[len(sorted_nums)//2-1])/2
        else:
            return sorted_nums[len(sorted_nums)//2]
        

            

print(Solution().findMedianSortedArrays([1,3],[2,7]))
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use two loops to find the two numbers that add up to the target
        """
       
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        # use dictionary to store the index of each number
        num_dict = {}

        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i



        return []
    
print(Solution().twoSum([2,7,11,15], 9))
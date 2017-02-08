class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtnArray = []
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if (nums[i] + nums[j] == target):
                    rtnArray =[i,j]
                    return rtnArray
                j += 1
        return rtnArray

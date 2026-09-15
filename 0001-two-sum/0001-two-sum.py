class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}

        for i in range(len(nums)):
            second_number=target-nums[i]
            if second_number in numbers:
                return [numbers[second_number],i]

            numbers[nums[i]]=i
        
        
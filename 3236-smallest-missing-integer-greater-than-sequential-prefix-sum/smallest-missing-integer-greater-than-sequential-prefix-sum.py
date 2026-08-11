class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Calculate the sum of the longest sequential prefix
        prefix_sum = nums[0]
        
        for i in range(1, len(nums)):
            # If the sequence breaks, stop adding
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
                
        # Step 2: Convert nums to a set for O(1) fast lookups
        nums_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= prefix_sum
        while prefix_sum in nums_set:
            prefix_sum += 1
            
        return prefix_sum

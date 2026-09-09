class Solution:
    def minOperations(self, nums: list[int]) -> int:

        operations = 0

        for i in range(1, len(nums)):

            # Current number must be greater than
            # the previous number
            if nums[i] <= nums[i - 1]:

                # Find how much we need to increase
                needed = nums[i - 1] - nums[i] + 1

                # Add the required operations
                operations += needed

                # Update the current number
                nums[i] += needed

        return operations
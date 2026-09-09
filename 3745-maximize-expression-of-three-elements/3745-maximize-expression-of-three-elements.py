class Solution:
    def maximizeExpressionOfThree(self, nums: list[int]) -> int:
        
        # Sort the numbers
        nums.sort()

        # Get the smallest number
        smallest = nums[0]

        # Get the largest number
        largest = nums[-1]

        # Get the second largest number
        second_largest = nums[-2]

        # Formula: largest + second largest - smallest
        answer = largest + second_largest - smallest

        return answer
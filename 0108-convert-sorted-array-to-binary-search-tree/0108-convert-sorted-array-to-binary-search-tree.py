# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums):

        # If the array is empty, return None
        if not nums:
            return None

        # Find the middle element
        mid = len(nums) // 2

        # Create the root node
        root = TreeNode(nums[mid])

        # Build the left subtree
        root.left = self.sortedArrayToBST(nums[:mid])

        # Build the right subtree
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        # Return the root
        return root
class Solution:
    def buildTree(self, inorder, postorder):

        if not inorder:
            return None

        # Last element of postorder is root
        root_value = postorder.pop()
        root = TreeNode(root_value)

        # Find root in inorder
        index = inorder.index(root_value)

        # Build right subtree first
        root.right = self.buildTree(inorder[index + 1:], postorder)

        # Build left subtree
        root.left = self.buildTree(inorder[:index], postorder)

        return root
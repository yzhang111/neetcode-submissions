# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        result,sub_result = [],[]
        self.serialize(root, result)
        self.serialize(subRoot, sub_result)

        result_str = ",".join(result)
        sub_str = ",".join(sub_result)
        return sub_str in result_str
        
    def serialize(self, root:Optional[TreeNode], result) -> None:
        if not root: 
            result.append('#')
            return

        result.append(str(root.val))
        self.serialize(root.left, result)
        self.serialize(root.right, result)

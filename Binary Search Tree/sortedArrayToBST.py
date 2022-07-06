# Time Complexity - O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBST(self,l,r,nums):
    if l<=r:
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.createBST(l, mid-1, nums)
        root.right = self.createBST(mid+1, r, nums)
        return root
    else:
        return None
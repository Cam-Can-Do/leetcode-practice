# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        nodes = []
        def dfs(root):
            nonlocal nodes
            if not root:
                nodes.append("N")
                return 
            else:
                nodes.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if nodes[i] == "N":
                i += 1
                return None
            node = TreeNode(int(nodes[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

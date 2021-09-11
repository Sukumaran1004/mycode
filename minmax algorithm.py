class Tree:  # create a class for the tree
    def __init__(self,data):  # constructor
        self.left=None
        self.right=None
        self.val=data

class Minmax:
    def solution(self,root,h,curheight):  # to find the solution using minmax algo
        if not root:
            return
        self.solution(root.left,h,curheight+1)
        self.solution(root.right,h,curheight+1)
        if(curheight<h):   # curheight is less than or not from the height of the tree
            if (curheight%2==0):  # if curheigth is even find max otherwise to find min
                if root.left and root.right:
                    root.val=max(root.left.val,root.right.val)
                elif root.left:
                    root.val=root.left.val
                elif root.right:
                    root.val=root.right.val
            else:
                if root.left and root.right:
                    root.val=min(root.left.val,root.right.val)
                elif root.left:
                    root.val=root.left.val
                elif root.right:
                    root.val=root.right.val

    def height(self,root):  # to find the height of the given tree
        if not root:
            return 0
        return(1+max(self.height(root.left),self.height(root.right)))

    def solve(self, root):
        h = self.height(root)
        self.solution(root, h, 0)
        return root



sol=Minmax()
root=Tree('a')
root.left=Tree('b')
root.right=Tree('c')
root.left.left=Tree('D')
root.left.right=Tree('E')
root.right.left=Tree('F')
root.right.right=Tree('G')
root.left.left.left=Tree(3)
root.left.left.right=Tree(5)
root.left.right.left=Tree(6)
root.left.right.right=Tree(9)
root.right.left.left=Tree(1)
root.right.left.right=Tree(2)
root.right.right.left=Tree(0)
root.right.right.right=Tree(-1)



sol.solve(root)

print("The result of the given tree using MINMAX ALGORITHM is ",root.val)










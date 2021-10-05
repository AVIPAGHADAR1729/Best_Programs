

class BinarySearchTree:

    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value



def insert(root,value):

    if root is None:
        return BinarySearchTree(value)
    else:
        if root.value == value:
            return root
        elif root.value < value:
            root.left = insert(root.left,value)
        elif root.value > value:
            root.right = insert(root.right,value)
            
    return root

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.value)
        printInOrder(root.right)



root = BinarySearchTree(50)

root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 


printInOrder(root)


    










    #BinaryTree problem #



class BinaryTree:


    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val



def sumOfTree(root):

    if root is None:
        return 0
    else:
        return root.val + sumOfTree(root.left) + sumOfTree(root.right)

def maxElTree(root):
    if root is None:
        return float(-1e7)
    else:
        leftSubTreeMax = maxElTree(root.left)
        rightSubTreeMax = maxElTree(root.right)
        return max(root.val,leftSubTreeMax,rightSubTreeMax)

def isElInTree(root,val):
    if root is None:
        return False
    else:
        isElInLeftSide = isElInTree(root.left,val)
        isElInRightSide = isElInTree(root.right,val)
        return root.val == val or isElInLeftSide or isElInRightSide

def heigthOfTree(root):

    if root is None:
        return 0
    else:
        return max(heigthOfTree(root.left),heigthOfTree(root.right)) + 1


def reverseTree(root):

    if root is None:
        return
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left,root.right = root.right,root.left

def printOrder(root):

    if root:
        printOrder(root.left)
        print(root.val)
        printOrder(root.right)
        
    
        






root = BinaryTree(10)
root.left = BinaryTree(20)
root.right = BinaryTree(30)
root.left.left = BinaryTree(50)
root.left.left.left = BinaryTree(100)
##
##print(heigthOfTree(root))
##
##printOrder(root)
##
##
##
####print(sumOfTree(root))
##
##
###print(float(-inf))
##
##print(maxElTree(root))
##print(isElInTree(root,1090))


printOrder(root)
print('Reverse')
reverseTree(root)
printOrder(rev)






















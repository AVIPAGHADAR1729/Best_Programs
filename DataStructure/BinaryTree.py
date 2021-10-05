

class BinaryTree:

    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    
        



def printInOrder(root):

    if root:
        printInOrder(root.left)
        print(root.value)
        printInOrder(root.right)

def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.value)

def printPreOrder(root):
    if root:
        print(root.value)
        printPreOrder(root.left)
        printPreOrder(root.right)




##
##root = BinaryTree(1)
##root.left = BinaryTree(2)
##root.right = BinaryTree(3)
##root.left.left = BinaryTree(4)
##root.left.right = BinaryTree(5)

##print(root)
##
####root.printInOrder(root)
##
##print(dir(root))
##
##printInOrder(root)


def sumOfTree(root):

    if root is None:
        return 0
    else:
        return root.value + sumOfTree(root.left) + sumOfTree(root.right)

def maxElTree(root):
    if root is None:
        return float(-1e7)
    else:
        leftSubTreeMax = maxElTree(root.left)
        rightSubTreeMax = maxElTree(root.right)
        return max(root.value,leftSubTreeMax,rightSubTreeMax)

def isElInTree(root,val):
    if root is None:
        return False
    else:
        isElInLeftSide = isElInTree(root.left,value)
        isElInRightSide = isElInTree(root.right,value)
        return root.val == val or isElInLeftSide or isElInRightSide

def heigthOfTree(root):

    if root is None:
        return 0
    else:
        return max(heigthOfTree(root.left),heigthOfTree(root.right)) + 1


def reverseBinaryTree(root):

    if root is None:
        return
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left,root.right = root.right,root.left

def printOrder(root):

    if root:
        printOrder(root.left)
        print(root.value)
        printOrder(root.right)


def invertBinaryTree(root):
    if root == None:
        return None
    else:
        temp = root
        invertBinaryTree(root.left)
        invertBinaryTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp


        

        
        
    
        






root = BinaryTree(10)
root.left = BinaryTree(20)
root.right = BinaryTree(30)
root.left.left = BinaryTree(50)
root.left.left.left = BinaryTree(100)

printOrder(root)
invertBinaryTree(root)
printOrder(root)




print(sumOfTree(root))


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


##printOrder(root)
##print('Reverse')
##reverseTree(root)
##printOrder(rev)

        
            
            
        
        

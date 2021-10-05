
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None


    def addAtBeg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def addAtEnd(self,data):

        if self.head is None:
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            tmp = self.head

            while tmp.next is not None:
                tmp = tmp.next
            node = Node(data)
            tmp.next = node
            node.next = None
            
        

    def printLL(self):
        if self.head:
            tmp = self.head
            while(tmp):
                print(tmp.data,end='-->')
                tmp = tmp.next
            print('None')
        else:
            print('Error')

    def delAtBeg(self):
        tmp = self.head
        self.head = tmp.next
        tmp = None

    def delAtEnd(self):

        if self.head is None:
            print('Error!!!')
        else:
            tmp= self.head
            while not tmp.next is None:
                tx = tmp
                tmp = tmp.next
            tx.next = None
            


    def delByValue(self,value):
        if self.head == None:
            print('Error!!!')
        
        temp = self.head

        while temp is not None:
            if temp.data == value:
                break
            tx = temp
            temp = temp.next

        tx.next = temp.next

        temp = None
    
    

        
        
        
def concat(ll1,ll2):
    t1,t2 = ll2.head,ll1.head
    dummy = Node(-1)
    temp = dummy

    while t1 or t2:
        if t1 and (not t2 or t1.data <= t1.data):
            temp.next = Node(t1.data)
            t1 = t1.next
        else:
            temp.next = Node(t2.data)
            t2 = t2.next
        
        temp = temp.next
        
    return dummy.next


def reverse(ll):
    tmp = ll.head
    prev,next_ = None,None

    while tmp is not None:
        next_ = tmp.next
        tmp.next = prev
        prev = tmp
        tmp = next_
        
    return prev


def Kreverse(ll,K):
    tmp = ll.head
    prev,next_ = None,None
    count = 0

    while tmp is not None and count < K:
        next_ = tmp.next
        tmp.next = prev
        prev = tmp
        tmp = next_
        count += 1

    if next_ is not None:
        temp.next = Kreverse(next_,K)
        
        
    return prev


def addDigitAsLL(lla,llb):
    dummy = Node(-1)
    l3 = dummy
    carry = 0
    while lla != None or llb != None:
        a = lla.data if lla != None else 0
        b = llb.data if llb != None else 0
        
        
        total = a + b + carry
        last_digit = total%10
        carry = total // 10

        
        
        l3.next = Node(last_digit)
        
        if lla != None:
            lla = lla.next
        if llb != None:
            llb = llb.next
        l3 = l3.next

        if carry > 0:
            l3.next = Node(carry)
            l3 = l3.next

    return dummy.next
        




lla = LinkedList()

lla.addAtEnd(1)
lla.addAtEnd(2)
lla.addAtEnd(3)

llb = LinkedList()

llb.addAtEnd(4)
llb.addAtEnd(4)
llb.addAtEnd(9)
llb.addAtEnd(7)

link = addDigitAsLL(lla.head,llb.head)



ll3 = LinkedList()
ll3.head = link

ll3.printLL()
    






##ll = LinkedList()
##
##ll.addAtEnd(100)
##ll.addAtEnd(200)
##ll.addAtEnd(300)
##
##
##revL = LinkedList()
##
##revL.head = Kreverse(ll,2)
##
##revL.printLL()
##
##
##
##
####
####ll.printLL()
######ll.delAtEnd()
######ll.delByValue(100)
####ll.printLL()
##
##
##ll1 = LinkedList()
##
##
##
##ll1.addAtEnd(200)
##ll1.addAtEnd(100)
##ll1.addAtEnd(300)
##ll1.addAtEnd(700)
##ll1.addAtEnd(600)
##
##ll2  = LinkedList()
##
##ll2.head = concat(ll,ll1)

##ll2.printLL()



##ll1.printLL()
##
##ll1.delAtBeg()
##
##ll1.printLL()
##        


    
            

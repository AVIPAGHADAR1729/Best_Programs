

## Queue using stack


class Queue:
    def __init__(self):
        self.st1 = []
        self.st2 = []



    def isEmpty(self,stack):
        return stack == []

    def enQ(self,value):
        self.st1.append(value)

    def deQ(self):
        if self.isEmpty(self.st1) and self.isEmpty(self.st2):
            return 'Error'
        else:
            if self.isEmpty(self.st2):
                while not self.isEmpty(self.st1):
                    self.st2.append(self.st1.pop())
            return self.st2.pop()
                
            

    


##q = Queue()
##
##q.enQ(10)
##q.enQ(20)
##q.enQ(30)
##q.enQ(40)
##q.enQ(50)
##
##print(q.deQ())
##print(q.deQ())
##print(q.deQ())
##print(q.deQ())
##print(q.deQ())


##  Queue usig LL


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class QueueWithLL:

    def __init__(self):
        self.front = None
        self.back = None


    def enQueue(self,data):
        node = Node(data)

        if self.front == None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node


    def isEmpty(self):
        return self.front == None

    def deQueue(self):

        if self.front == None:
            print('Error')
        else:
            tmp = self.front
            self.front = self.front.next
            tmp = None
            
        

    def peek(self):
        return self.front.data

    def printQueue(self):
        mvr = self.front

        while mvr != None:
            print(mvr.data,end='|')
            mvr = mvr.next
        print()
        
            
        
    
            
            
qll = QueueWithLL()

qll.enQueue(100)
qll.enQueue(200)
qll.enQueue(300)
qll.enQueue(400)
qll.enQueue(500)
qll.enQueue(600)

##qll.printQueue()
##qll.deQueue()
##qll.deQueue()
##
##print(qll.peek())
##
##qll.printQueue()
        
#############################################################################

# stack using LL

class StackWithLL:

    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            node.next =  self.head
            self.head = node
            

    def pop(self):

        if self.head == None:
            print('Error!!')
        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next= None
            return self.head.data
            

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.head == None

    def printStack(self):
        mvr = self.head

        while mvr != None:
            print(mvr.data,end='<-')
            mvr = mvr.next
        print()
        
        




##sll = StackWithLL()
##
##sll.push(100)
##sll.push(200)
##sll.push(300)
##sll.push(400)
##sll.push(500)
##sll.push(600)
##
##sll.printStack()
##
##
##
##print(sll.pop())
##print(sll.pop())
##sll.printStack()


        
            
            
                    

        
        

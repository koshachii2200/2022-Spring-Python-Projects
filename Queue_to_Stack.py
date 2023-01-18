class Queue(object):
    '''Queue implements the FIFO principle.'''

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):                                            #runtime: O(n)
        if (not self.isEmpty()):
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)

class Stack(object):
    '''Stack implements the LIFO principle.'''

    def __init__(self):                                           #runtime: O(1)
        self.queue1=Queue()
        self.queue2=Queue()

    def push(self,item):                                          #runtime: O(1)
        self.queue1.enqueue(item)

    def peek(self):                                               #runtime: O(n^2)
        if self.queue1.isEmpty():return None
        while self.queue1.size()>1:
            self.queue2.enqueue(self.queue1.dequeue())            #enqueue all elements of queue1 to queue2 except last element
        last=self.queue1.dequeue()                                #save last element of queue1 as popped element using dequeue
        self.queue1,self.queue2=self.queue2,self.queue1
        self.queue1.enqueue(last)                                 #put last back in queue1
        return last

    def pop(self):                                               #runtime: O(n^2)
        if self.queue1.isEmpty():return None
        while self.queue1.size()>1:
            self.queue2.enqueue(self.queue1.dequeue())           #enqueue all elements of queue1 to queue2 except last element
        last=self.queue1.dequeue()                               #save last element of queue1 as popped element using dequeue
        self.queue1,self.queue2=self.queue2,self.queue1
        return last

    def isEmpty(self):                                           #runtime: O(1)
        return self.queue1.isEmpty()

    def size(self):                                              #runtime: O(1)
        return self.queue1.size()

    def __str__(self):                                           #runtime: O(n)
        return self.queue1.__str__()


###############################
#                             #
#   Example run of a Stack    #
#                             #
###############################

"""stack=Stack()

stack.push(10)
print(stack)

stack.push(18)
stack.push(1024)
print(stack)

stack.peek()
print(stack.peek())
stack.pop()
print(stack)"""
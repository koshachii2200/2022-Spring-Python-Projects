class Stack (object):

  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    if(not self.isEmpty()):
      return self.stack.pop()
    else:
      return None

  # check what item is on top of the stack without removing it
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size(self):
    return (len(self.stack))

  # a string representation of this stack.
  def __str__(self):
    return str(self.stack)

class Queue(object):
  '''Queue implements the FIFO principle.'''

  def __init__(self):                           #runtime: O(1)
    self.stack1=Stack()
    self.stack2=Stack()

  def enqueue(self, item):                      #runtime: O(1)
    self.stack1.push(item)

  def dequeue(self):                            #runtime: O(n)
    if self.stack1.isEmpty():return None
    while not self.stack1.isEmpty():
      self.stack2.push(self.stack1.pop())
    top=self.stack2.pop()
    while not self.stack2.isEmpty():
      self.stack1.push(self.stack2.pop())
    return top

  def isEmpty(self):                            #runtime: O(1)
    return self.stack1.isEmpty()

  def size(self):                               #runtime: O(1)
    return self.stack1.size()

  def __str__(self):                            #runtime: O(n)
    return self.stack1.__str__()


###############################
#                             #
#   Example run of a Queue    #
#                             #
###############################

"""queue=Queue()

queue.enqueue(10)
print(queue)

queue.enqueue(18)
queue.enqueue(1024)
print(queue)

queue.dequeue()
print(queue)"""
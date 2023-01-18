class Link(object):
    ''' This class represents a link between data items only'''

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " --> " + str(self.next)


class LinkedList(object):
    ''' This class implements the operations of a simple linked list'''

    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        '''inset data at begining of a linked list'''
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    def insertLast(self, data):
        ''' Inset the data at the end of a linked list '''
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return
        # find the last and insert it there
        while (current.next != None):
            current = current.next

        current.next = newLink

    def findLink(self, data):
        ''' find to which data is the link of a given data inside this linked list'''
        current = self.first
        if (current == None):
            return None

        # search and find the position of the given data, the get the link if it exists
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    def deleteLink(self, data):
        ''' Removes the data from the list if exist and fix the link problems.'''

        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current

            current = current.next

            if (current == self.first):
                self.first = self.first.next
            else:
                previous.next = current.next

        return current

    def __str__(self):
        return str(self.first)

class Stack(object):
    '''Stack implements the LIFO principle.'''

    def __init__(self):                                           #runtime: O(1)
        self.list=LinkedList()

    def push(self,item):                                          #runtime: O(1)
        self.list.insertFirst(item)

    def peek(self):                                               #runtime: O(1)
        if self.isEmpty():return None
        return self.list.first.data

    def pop(self):                                                #runtime: O(1)
        if self.isEmpty():return None
        top=self.list.first.data
        if not self.list.first.next:self.list.first=None
        else:self.list.first=self.list.first.next
        return top

    def isEmpty(self):                                           #runtime: O(1)
        return not self.list.first

    def size(self):                                              #runtime: O(n)
        current=self.list.first
        if self.list.isEmpty():return 0
        count=1
        while current.next:
            count+=1
            current=current.next
        return count

    def __str__(self):                                           #runtime: O(n)
        return self.list.__str__()


#############################
#                           #
#   Example run of Stack    #
#                           #
#############################

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
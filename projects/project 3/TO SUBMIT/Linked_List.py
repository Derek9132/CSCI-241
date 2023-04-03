class Linked_List:
    
    class __Node:
        
        def __init__(self, val, next=None, prev=None):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = next
            self.prev = prev

            def get_val(self):
                return self.val
            
            def set_val(self, val):
                self.val = val
            
            def get_next(self):
                return self.next
            
            def set_next(self, next):
                self.next = next

            def get_prev(self):
                return self.prev
            
            def set_prev(self, prev):
                self.prev = prev
            #This is the node class for the linked list, which has two leading underscores to ensure it is not used outside of the Linked_List class.
            #The constructor for the node class has 3 attributes: the node's value (val) and references to the previous and next nodes(prev and next).
            #The prev attribute is found in doubly linked lists but not singly linked lists.
            #I put in accessor and mutator methods when I first opened the project because I didn't know what else to write, but wanted to write something.
            #As it turns out, the mutators and accessors were not needed. Do these unnecessary methods hinder performance? 
                

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__size = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__header.prev = None
        self.__trailer.prev = self.__header
        self.__trailer.next = None
        #This is the constructor for the Linked_List class. The linked list has a size attribute, a header node and a trailer node.
        #Each linked list is constructed with two nodes, a header and a trailer, which do not contain any data and instead act as references to the start and end.
        #Because this is a doubly linked list, the header points to the trailer, but the trailer also points to the header.

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size
    #The performance of this function is O(1) as it just returns the self.__size attribute that has updates
    # in accordance with appending and removing elements.

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new = Linked_List.__Node(val)
        self.__trailer.prev.next = new
        new.prev = self.__trailer.prev
        new.next = self.__trailer
        self.__trailer.prev = new
        self.__size += 1
    #This function has O(1) performance thanks to the linked list's doubly linked nature. 
    #No matter the input size, the algorithm will always take the same amount of time to complete, as it only focuses on the trailing end of the list.
    #With a singly linked list, performance would have been O(n) because the iteration would have to start at the head and visit each node until the end.
    #This method, in my opinion, best showcases the advantage of a doubly linked list.

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if self.__size <= index or index < 0:
            raise IndexError
        new = Linked_List.__Node(val)
        i = 0
        if index >= (self.__size//2):
            cur = self.__trailer.prev
            while i < (self.__size - index):
                cur = cur.prev
                i += 1
            new.prev = cur
            new.next = cur.next
            cur.next.prev = new
            cur.next = new
        else:
            cur = self.__header.next
            while i < index:
                cur = cur.next
                i += 1
            new.prev = cur.prev
            cur.prev.next = new
            new.next = cur
            cur.prev = new
        self.__size += 1
        #The performance of the remove_element function is O(n), linear time. 
        #The time it takes for the algorithm to complete increases with the size of the input.
        #This is somewhat alleviated by the fact that the iteration can start on either end, but the worst case for this function is still O(n).
        #To prevent nodes from being added at the tail position with this method, an IndexError is raised when the given index is greater than OR EQUAL TO self.__size.


    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if self.__size <= index or index < 0:
            raise IndexError
        i = 0
        if index >= (self.__size//2):
            cur = self.__trailer
            while i < (self.__size - index):
                cur = cur.prev
                i += 1
            removed_val = cur.val
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.next = None
            cur.prev = None
        else:
            cur = self.__header.next
            while i < index:
                cur = cur.next
                i += 1
            removed_val = cur.val
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.next = None
            cur.prev = None
        self.__size -= 1
        return removed_val
    #The performance of the remove_element function is O(n), linear time. 
    #The time it takes for the algorithm to complete increases with the size of the input.
    #This is somewhat alleviated by the fact that the iteration can start on either end, but the worst case for this function is still O(n).
    #I built a delete method, but I don't see how it would improve performance,so I scrapped it.
    
    #def delete(self, Node):
            #Node.prev.next = Node.next
            #Node.next.prev = Node.prev
            #Node.next = None
            #Node.prev = None
            #return None        
        
    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if self.__size <= index or index < 0:
            raise IndexError
        i = 0
        if index >= (self.__size//2):
            cur = self.__trailer
            while i < (self.__size - index):
                cur = cur.prev
                i += 1
        else:
            cur = self.__header.next
            while i < index:
                cur = cur.next
                i += 1
        return cur.val
        #The performance of the get_element function is O(n), linear time. 
        #The time it takes for the algorithm to complete increases with the size of the input.
        #This is somewhat alleviated by the fact that the iteration can start on either end, but the worst case for this function is still O(n).
        #Drawing out the linked lists on paper really helped me out for the get, insert, and remove methods.

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size == 0 or self.__size == 1:
            pass
        else:
            first_val = self.__header.next.val
            self.__header.next = self.__header.next.next
            self.__header.next.prev = self.__header
            self.append_element(first_val)
            self.__size -= 1
        #This function's performance is O(1), constant time. The algorithm will take the same time to complete regardless of the linked list's size.
        #The function append_element within the rotate_left function also operates in constant time. 
        #Just like how a constant multiplied by another constant is still a constant, an O(1) function within an O(1) function is still O(1).
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self.__size == 0:
            return '[' + ' ' + ']'
        elif self.__size == 1:
            return '[ ' + str(self.__header.next.val) + ' ]'
        else:
            list_Contents = []
            cur = self.__header.next
            while cur.next != None:
                list_Contents.append(cur.val)
                cur = cur.next
            str_rep = '[ '+ ', '.join(str(i) for i in list_Contents) + ' ]'
            return str_rep
        #The performance of this function is O(n).
        #Any method that requires getting each element of the linked list or visiting every node will be at least linear time O(n).

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__iter_index = self.__header.next
        self.__counter = 0
        return self
        #In an array, the starting point of an iteration is index=0, arr[0]
        #In a linked list, the starting point of an iteration is the node that comes immediately after the header node, self.__header.next
        #It could also be the node that comes immediately before the trailer node, self.__trailer.prev.
        #I'd like to know how a for loop would iterate if the __iter__ method started at the node before the trailer node. Is it possible to have 2 __iter__ methods?

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__counter == self.__size:
            raise StopIteration
        to_return = self.__iter_index.val
        self.__iter_index = self.__iter_index.next
        self.__counter += 1
        return to_return
        #In an array, the __next__ method would get the value at arr[i] and increment i by 1 until i equals len(arr).
        #In a linked list, there are no defined indices, so the index must be stored in a separate variable as the __next__ method traverses the list.
        #With each iteration, the value of the current node is returned, the current node is changed to current node.next, and the counter is incremented by 1.
        #Notice the counter variable is independent/separate from the value of the current node, unlike an array.

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        reverseList = Linked_List()
        cur = self.__trailer.prev
        while cur.prev != None:
            reverseList.append_element(cur.val)
            cur = cur.prev
        return reverseList
        #Any method that requires getting each element of the linked list or visiting every node will be at least linear time O(n).
        #Here, the while loop will run once for each node in the linked list, so there is a linear relationship between the input size and algorithm's duration.

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    dllist1 = Linked_List()
    dllist2 = Linked_List()
    dllist3 = Linked_List()
    dllist1.append_element(4)
    dllist1.append_element(5)
    dllist1.append_element(6)
    dllist1.append_element(7)
    dllist1.append_element(8)
    dllist1.append_element(9)   
    dllist2.append_element(12) 
    reverse1 = reversed(dllist1)
    left1 = dllist1.rotate_left()
    left3 = dllist3.rotate_left()
    a = dllist1.get_element_at(4)
    b = dllist1.remove_element_at(2)
    c = dllist1.remove_element_at(5)
    x = str(dllist1)
    y = str(dllist2)
    z = str(dllist3)
    d = dllist2.remove_element_at(0)
    v = str(dllist2)
    dllist2.append_element(8)
    dllist2.append_element(2)
    dllist3.append_element(4)
    dllist1.insert_element_at(3,2)
    s = str(dllist2)
    t = str(dllist3)
    u = dllist1
    #I did most of my testing in a python visualizer (python tutor) to see each of my program's steps and executions.
    #I copied my test code from python tutor into here.
    #I made sure to do test cases for every possible case I could think of
    #dllist1 has multiple elements, dllist2 has one element, and dllist3 is empty
    #For dllist1, I decided to try the reverse and rotate_left methods first before moving onto other methods
    #I tested out removing elements before inserting them
    






from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    # TODO replace pass with any additional initializations you need.
    self.__front = 0
    self.__back = 0
    self.__size = 0
    #This is the constructor for the Array_Deque class. It initializes an array with a single cell that contains None.
    #It also initializes variables for the array's front and back index, which both point to the array's single cell.
    #It also initializes a self.__size variable to be used as a quicker substitute to len().
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    # Orient your string from front (left) to back (right).
    if self.__size == 0:
      return '[ ]'
    elif self.__size == 1:
      return '[ ' + str(self.__contents[self.__front]) + ' ]'
    else:
      contentList = []
      deque_index = self.__front
      while deque_index%self.__capacity != (self.__back%self.__capacity):
        if self.__contents[deque_index%self.__capacity] != None:
          contentList.append(self.__contents[deque_index%self.__capacity])
        deque_index += 1
      contentList.append(self.__contents[self.__back%self.__capacity])
      return '[ '+ ', '.join(str(i) for i in contentList) + ' ]'
    #The str() function runs in O(n^2) time. Each element in the array must be visited and appended to a separate list, 
    #and the string concatenation is itself O(n) in the worst case, so the str() function is O(n^2).
      

    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    if self.__size == 0:
      return 0
    elif self.__front%self.__capacity > self.__back%self.__capacity:
      return self.__capacity - (self.__front%self.__capacity - self.__back%self.__capacity) + 1
    else:
      return (self.__back%self.__capacity - self.__front%self.__capacity) + 1
    #This len() function is able to run in constant time because it involves simple comparisons and operations with constants. 
    #Keeping track of the front and back indices circumvents the need to visit every cell in the array.
    

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is it
    # necessary?)
    bigger_arr = [None] * (self.__capacity * 2)
    for i in range(self.__capacity):
      bigger_arr[i] = self.__contents[(i + self.__front)%self.__capacity]
    self.__contents = bigger_arr
    self.__front = 0
    self.__back = self.__capacity - 1
    self.__capacity += self.__capacity
    return self.__contents
  #The grow() function runs in O(n) linear time. The function takes a constant number of steps plus a for loop which
  # takes additional steps that scale linearly with the input size. The graph representing this performance would be a linear
  #line with a y intercept greater than 0.
    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == 0:
      self.__contents[self.__front%self.__capacity] = val
    elif (self.__front - 1)%self.__capacity == self.__back:
      self.__grow()
      self.__contents[(self.__front - 1)%self.__capacity] = val
      self.__front = (self.__front - 1)%self.__capacity
    else:
      self.__contents[(self.__front - 1)%self.__capacity] = val
      self.__front = (self.__front - 1)%self.__capacity
    self.__size += 1
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return None
    else:
      front_value = self.__contents[self.__front%self.__capacity]
      self.__contents[self.__front%self.__capacity] = None
      if self.__front%self.__capacity != self.__back%self.__capacity:
        self.__front = (self.__front + 1)%self.__capacity
      self.__size -= 1
      return front_value
  

  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return None
    else:
      return self.__contents[self.__front%self.__capacity]
    #The push,pop, and peek front methods all run in constant time O(1). Operations at the very front of the array
    # can run in constant time because the array does not need to be traversed, meaning the size of the array is negligible.
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == 0: 
      self.__contents[self.__back%self.__capacity] = val
    elif (self.__back + 1)%self.__capacity == self.__front:
      self.__grow()
      self.__contents[(self.__back + 1)%self.__capacity] = val
      self.__back = (self.__back + 1)%self.__capacity
    else:
      self.__contents[(self.__back + 1)%self.__capacity] = val
      self.__back = (self.__back + 1)%self.__capacity
    self.__size += 1

  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size == 0:
      return None
    else:
      back_value = self.__contents[self.__back%self.__capacity]
      self.__contents[self.__back%self.__capacity] = None
      if self.__front%self.__capacity != self.__back%self.__capacity:
        self.__back = (self.__back - 1)%self.__capacity
      self.__size -= 1
      return back_value

  def peek_back(self):
    # TODO replace pass with your implementation.
    if self.__size == 0:
      return None
    else:
      return self.__contents[self.__back%self.__capacity]
    #The push,pop, and peek back methods all run in constant time O(1). Operations at the very back of the array
    # can run in constant time because the array does not need to be traversed, meaning the size of the array is negligible.

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass

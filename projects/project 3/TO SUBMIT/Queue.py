from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from front (left) to back (right).
    return str(self.__dq)
  #The str function is O(n^2) quadratic time in both the linked list and array implementations of
  #the deque, so it will be O(n^2) quadratic time in the queue class.

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)
  #The len function is O(1) constant time in both the linked list and array implementations of
  #the deque, so it will be O(1) constant time in the queue class.

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_back(val)
    #The push_back function is O(1) constant time in both the linked list and array implementations of
    #the deque, so it will be O(1) constant time in the queue class.

  def dequeue(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_front()
  #The pop_front function is O(1) constant time in both the linked list and array implementations of
  #the deque, so it will be O(1) constant time in the queue class.

  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_front()
  #The peek_front function is O(1) constant time in both the linked list and array implementations of
  #the deque, so it will be O(1) constant time in the queue class.

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  

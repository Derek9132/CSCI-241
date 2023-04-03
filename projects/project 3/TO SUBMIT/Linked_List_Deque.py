from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  #This is the constructor for the Deque class when using linked lists. Creating the linked list instance is O(1),
  #the str() function runs in O(n^2), and the len() function runs in O(1).

  def push_front(self, val):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val, 0)
    #Both the append_element method and the insert_element_at method when inserting at 0 run in constant time, which makes
    #the push_front method constant time O(1).
  
  def pop_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      return None
    front_val = self.__list.remove_element_at(0)
    return front_val
  #The index of the remove element_at method is always 0 for the purposes of the pop_front method, so remove_element_at
  # is always O(1) and pop_front() is always O(1).

  def peek_front(self):
    # TODO replace pass with your implementation.
    # Use the head position for the front.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.get_element_at(0)
    #The peek_front method runs in constant time O(1) because regardless of the list's
    #size, it only deals with one node located at the very front, in the same location
    #in every possible case.

  def push_back(self, val):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    self.__list.append_element(val)
    #The push_back method runs in constant time O(1) because regardless of the list's
    #size, it only adds one node at the very back, in the same location every time.
  
  def pop_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if len(self.__list) == 0:
      return None
    back_val = self.__list.remove_element_at(len(self.__list) - 1)
    return back_val
  #The pop_back method runs in constant time O(1) because regardless of the list's
    #size, it only deals with one node located at the very back, in the same location
    #in every possible case.

  def peek_back(self):
    # TODO replace pass with your implementation.
    # Use the tail position for the back.
    if len(self.__list) == 0:
      return None
    else:
      return self.__list.get_element_at(len(self.__list) - 1)
    #The peek_back method runs in constant time O(1) because regardless of the list's
    #size, it only deals with one node located at the very back, in the same location
    #in every possible case.

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass

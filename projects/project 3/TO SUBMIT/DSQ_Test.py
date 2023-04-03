import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should be in a method whose name begins with test_

  def test_empty(self):
    return str(self.__queue) + str(self.__stack)
  
  def test_empty_get(self):
    return str(self.__queue.peek()) + str(self.__stack.peek())
  
  def test_empty_remove(self):
    return str(self.__queue.dequeue()) + str(self.__stack.pop())
  
  def test_add_one(self, val):
    self.__stack.push(val)
    self.__queue.enqueue(val)
    return str(self.__queue) + str(self.__stack)
  
  def test_add_five(self,a,b,c,d,e):
    self.__stack.push(a)
    self.__queue.enqueue(a)
    self.__stack.push(b)
    self.__queue.enqueue(b)
    self.__stack.push(c)
    self.__queue.enqueue(c)
    self.__stack.push(d)
    self.__queue.enqueue(d)
    self.__stack.push(e)
    self.__queue.enqueue(e)
    return str(self.__queue) + str(self.__stack)
  
  def test_get(self,a,b,c):
    self.__stack.push(a)
    self.__queue.enqueue(a)
    self.__stack.push(b)
    self.__queue.enqueue(b)
    self.__stack.push(c)
    self.__queue.enqueue(c)
    return str(self.__stack.peek()) + str(self.__queue.peek())
  
  def test_remove(self,a,b,c):
    self.__stack.push(a)
    self.__queue.enqueue(a)
    self.__stack.push(b)
    self.__queue.enqueue(b)
    self.__stack.pop()
    self.__queue.dequeue()
    return str(self.__stack.peek()) + str(self.__queue.peek())
  
  def test_remove_3(self,a,b,c):
    self.__stack.push(a)
    self.__queue.enqueue(a)
    self.__stack.push(b)
    self.__queue.enqueue(b)
    self.__stack.push(c)
    self.__queue.enqueue(c)
    self.__stack.pop(a)
    self.__queue.dequeue()
    self.__stack.pop()
    self.__queue.dequeue()
    self.__stack.pop()
    self.__queue.dequeue()
    return str(self.__stack.peek()) + str(self.__queue.peek())

    
    
  

if __name__ == '__main__':
  unittest.main()


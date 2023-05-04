class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the methods.

    def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
      self.height = 1
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None


  def __rotate_left__(self, root):
    floater = root.right.left
    root.right.left = root
    root = root.right
    root.left.right = floater
    self.__heightUpdate__(root.left)
    self.__heightUpdate__(root)
    return root 
  #This is a supporting method used to balance the BST. It runs in constant time O(1) as it simply rearranges two nodes.

  def __rotate_right__(self, root):
    floater = root.left.right
    root.left.right = root
    root = root.left
    root.right.left = floater
    self.__heightUpdate__(root.right)
    self.__heightUpdate__(root)
    return root 
  #This is a supporting method used to balance the BST. It runs in constant time O(1) as it simply rearranges two nodes.

  def __height_return__(self, root):
      if root == None:
          return 0
      return root.height
  #This is a supporting method used to balance the BST. It runs in constant time O(1) as it returns 0 or the root's height.
    
  def __balanced__(self,root):
    if root == None:
      return
    elif self.__height_return__(root.right) - self.__height_return__(root.left) == 2:
      if self.__height_return__(root.right.right) - self.__height_return__(root.right.left) < 0:
          root.right = self.__rotate_right__(root.right)
      root = self.__rotate_left__(root)
    elif self.__height_return__(root.right) - self.__height_return__(root.left) == -2:
      if self.__height_return__(root.left.right) - self.__height_return__(root.left.left) > 0:
          root.left = self.__rotate_left__(root.left)
      root = self.__rotate_right__(root)
    return root
  #The balance method runs in constant time O(1).It only rearranges two nodes at a time, so the size of the tree does not matter.

  def __heightUpdate__(self, root):
      if root.left == None and root.right == None:
          root.height = 1
      elif root.left != None and root.right != None:
          if root.left.height > root.right.height:
              root.height = root.left.height + 1
          else:
              root.height = root.right.height + 1
      elif root.left != None:
          root.height = root.left.height + 1
      else:
          root.height = root.right.height + 1
  #The __heightUpdate__() method is used in the recursive removal method to properly update the height. It runs in O(1) constant time as it only involves conditionals 
  #and adding/subtracting numbers

  def __insertRecursive__(self, value, root):
    if root == None:
      root = Binary_Search_Tree.__BST_Node(value)
      return root
    else:
      if value > root.value:
        root.right = self.__insertRecursive__(value, root.right)
        root = self.__balanced__(root)
        if root.height > root.right.height + 1:
            root.height = root.height
        else:
            root.height = root.right.height + 1
        return root
      elif value < root.value:
        root.left = self.__insertRecursive__(value, root.left)
        root = self.__balanced__(root)
        if root.height > root.left.height + 1:
            root.height = root.height
        else:
            root.height = root.left.height + 1
        return root
    raise ValueError
  
  def __removeRecursive__(self, value, root):
    if root == None:
      raise ValueError
    elif root.value == value:
      if root.right == None and root.left == None:
          return None
      elif root.right != None and root.left != None:
          val = root.value
          lowest_right = self.__minValue__(root.right)
          root = self.__removeRecursive__(lowest_right, root)
          self.__find_value__(val, root).value = lowest_right
          return root
      else:
          if root.left != None:
              return root.left
          else:
              return root.right
    else:
          if value > root.value:
            root.right = self.__removeRecursive__(value, root.right)
            root = self.__balanced__(root)
            self.__heightUpdate__(root)
            return root
          elif value < root.value:
            root.left = self.__removeRecursive__(value, root.left)
            root = self.__balanced__(root)
            self.__heightUpdate__(root)
            return root
        
  def __minValue__(self, root):
    while root.left != None:
        root = root.left
    return root.value
  #The __minValue__() is used to support the removal function.
  # This function runs in O(log n) time. It eliminates half the tree with each loop iteration, specifically the right half.

  def __find_value__(self, value, root):
    while root.value != value:
        if value > root.value:
            root = root.right
        elif value < root.value:
            root = root.left
    return root
    #The __find_value__() method is used to get the correct node reference after a rotation.
    #It runs in O(log n), as half of each subtree is eliminated every time the loop runs.

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation

    if self.__root == None:
      self.__root = Binary_Search_Tree.__BST_Node(value)
    else:
      self.__root = self.__insertRecursive__(value, self.__root)
  #The insert method runs in O(log n) time because the recursive insert method runs in O(log n) time as well. 
  #When looking for the place where a value should be inserted, half the tree is eliminated with each recursive call, which allows for O(log n) time complexity.

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation
    if self.__root == None:
        raise ValueError
    else: 
        self.__root = self.__removeRecursive__(value, self.__root)
 #The remove method runs in O(log n) time because the recursive remove method runs in O(log n) time as well. 
 #When looking for the place where a value should be removed, half the tree is eliminated with each recursive call, which allows for O(log n) time complexity.


  def __inOrderRecursive__(self, root):
    if root == None:
        return ''
    else:
        return self.__inOrderRecursive__(root.left) + ' ' +  str(root.value) + ' ' + self.__inOrderRecursive__(root.right)
  
  def __preOrderRecursive__(self, root):
    if root == None:
        return ''
    else:
        return str(root.value) + ' ' + self.__preOrderRecursive__(root.left) + ' ' + self.__preOrderRecursive__(root.right)
  
  def __postOrderRecursive__(self, root):
    if root == None:
        return ''
    else:
        return self.__postOrderRecursive__(root.left) + ' ' + self.__postOrderRecursive__(root.right) + ' ' + str(root.value)

  def __toListRecursive__(self, root):
    if root == None:
        return []
    else:
        return self.__toListRecursive__(root.left) + [(root.value)] +  self.__toListRecursive__(root.right)
  
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
    if self.__root == None:
       return '[ ' + ']' 
    elif self.__root.height == 1:
       return '[ ' + str(self.__root.value) + ' ]'
    else:
       return_list = self.__inOrderRecursive__(self.__root).split(' ')
       return '[ '+ ', '.join(i for i in return_list if i != '') + ' ]'
    #The in_order method and its private recursive method run in O(n) linear time. I have tested it with 5, 7, and 9 nodes and plotted the points on desmos.
    #For 5 nodes the in_order method takes 75 steps, for 7 it takes 99, and for 9 it takes 123 (+12 steps per node). 

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
      if self.__root == None:
        return '[ ' + ']' 
      elif self.__root.height == 1:
        return '[ ' + str(self.__root.value) + ' ]'
      else:
        return_list = self.__preOrderRecursive__(self.__root).split(' ')
        return '[ '+ ', '.join(i for i in return_list if i != '') + ' ]'
    #The pre_order method and its private recursive method run in O(n) linear time. 4
    #It takes the same number of steps as the in_order function for 5,7, and 9 nodes, so I will assume it is also linear.

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation
      if self.__root == None:
        return '[ ' + ']' 
      elif self.__root.height == 1:
        return '[ ' + str(self.__root.value) + ' ]'
      else:
        return_list = self.__postOrderRecursive__(self.__root).split(' ')
        return '[ '+ ', '.join(i for i in return_list if i != '') + ' ]'
    #The post_order method and its private recursive method run in O(n) linear time. 4
    #It takes the same number of steps as the in_order and pre_order functions for 5,7, and 9 nodes, so I will assume it is also linear.



  def to_list(self):
    # Construct and return a Python list/array containing the in-order
    # traversal of the tree. Your solution must be recursive. This will
    # involve the introduction of additional private methods to support
    # the recursion control variable.
    if self.__root == None:
       return []
    elif self.__root.height == 1:
       return [self.__root.value]
    else:
       return self.__toListRecursive__(self.__root)# TODO replace pass with your implementation
    #The to_list method and its private recursive method run in O(n) linear time. I have tested it with 5, 7, and 9 nodes and plotted the points on desmos.
    #For 5 nodes the in_order method takes 50 steps, for 7 it takes 66, and for 9 it takes 82 (+8 steps per node). 

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root == None:
       return 0
    return self.__root.height # TODO replace pass with your implementation
  #The get_height() method runs in constant time as all it does is return 0 or the height of self.__root.

  def __str__(self):
    return self.in_order()
  #Because the in_order() method runs in O(n) linear time, the __str__ method will also run in linear time.

if __name__ == '__main__':
  test_bst = Binary_Search_Tree()
  test_bst.insert_element(50)
  test_bst.insert_element(60)
  test_bst.insert_element(40)
  test_bst.insert_element(55)
  test_bst.insert_element(65)
  test_bst.insert_element(52)
  test_bst.insert_element(53)
  test_bst.remove_element(65)
  print(test_bst.in_order())


import unittest
from Binary_Search_Tree import Binary_Search_Tree


class BST_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    def test_empty(self):
        return str(self.__tree)
    
    def test_empty_list(self):
        return self.__tree.to_list()
    
    def test_insert_error(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(60)
        self.__tree.insert_element(40)
        self.__tree.insert_element(50)
    
    def test_insert(self):
        self.__tree.insert_element(80)
        self.__tree.insert_element(90)
        self.__tree.insert_element(100)
        self.__tree.insert_element(98)
        self.__tree.insert_element(105)
        self.__tree.insert_element(96)
        self.__tree.insert_element(82)
        self.__tree.insert_element(78)
        self.__tree.insert_element(84)
        self.__tree.insert_element(110)
        self.__tree.insert_element(108)
        return self.__tree.in_order() + self.__tree.pre_order() + self.__tree.post_order() + ' ' +  str(self.__tree.get_height())
    
    def test_insert_list(self):
        self.__tree.insert_element(80)
        self.__tree.insert_element(90)
        self.__tree.insert_element(100)
        self.__tree.insert_element(98)
        self.__tree.insert_element(105)
        self.__tree.insert_element(96)
        self.__tree.insert_element(82)
        self.__tree.insert_element(78)
        self.__tree.insert_element(84)
        self.__tree.insert_element(110)
        self.__tree.insert_element(108)
        return self.__tree.to_list()

    def test_remove_error(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(60)
        self.__tree.insert_element(40)
        self.__tree.remove_element(70)

    def test_remove(self):
        self.__tree.insert_element(90)
        self.__tree.insert_element(80)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(95)
        self.__tree.insert_element(105)
        self.__tree.insert_element(110)
        self.__tree.remove_element(95)
        self.__tree.insert_element(70)
        self.__tree.insert_element(80)
        return self.__tree.in_order() + self.__tree.pre_order() + self.__tree.post_order() + ' ' +  str(self.__tree.get_height())
    
    def test_remove_list(self):
        self.__tree.insert_element(90)
        self.__tree.insert_element(80)
        self.__tree.insert_element(100)
        self.__tree.insert_element(70)
        self.__tree.insert_element(95)
        self.__tree.insert_element(105)
        self.__tree.insert_element(110)
        self.__tree.remove_element(95)
        self.__tree.insert_element(70)
        self.__tree.insert_element(80)
        return self.__tree.to_list()
    
    def test_insert_2(self):
        self.__tree.insert_element(60)
        self.__tree.insert_element(50)
        self.__tree.insert_element(40)
        self.__tree.insert_element(48)
        self.__tree.insert_element(38)
        self.__tree.insert_element(46)
        self.__tree.insert_element(36)
        self.__tree.insert_element(34)
        self.__tree.insert_element(66)
        self.__tree.insert_element(68)
        self.__tree.insert_element(70)
        return self.__tree.in_order() + self.__tree.pre_order() + self.__tree.post_order() + ' ' +  str(self.__tree.get_height())
    
    def test_remove_2(self):
        self.__tree.insert_element(70)
        self.__tree.insert_element(36)
        self.__tree.insert_element(82)
        self.__tree.insert_element(40)
        self.__tree.insert_element(80)
        self.__tree.insert_element(100)
        self.__tree.insert_element(95)
        self.__tree.remove_element(70)
        self.__tree.remove_element(36)
        self.__tree.remove_element(40)
        return self.__tree.in_order() + self.__tree.pre_order() + self.__tree.post_order() + ' ' +  str(self.__tree.get_height())


    




if __name__ == '__main__':
  unittest.main()

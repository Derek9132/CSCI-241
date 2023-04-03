import sys # for sys.argv, the command-line arguments

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
    open = ['(', '{', '[']
    closed = [')', '}', ']']
    delim_stack = []
    for i in filename:
      if i in open:
        delim_stack.append(i)
      elif i in closed:
        if len(delim_stack) > 0 and closed.index(i) == open.index(delim_stack[len(delim_stack) - 1]):
          delim_stack.pop()
        else: 
          return False
    if len(delim_stack) == 0:
        return True
    else: 
        return False

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')



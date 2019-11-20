import sys
from string import ascii_lowercase

valid_words = None
path = []

def clean_word(word):
    for letter in word:
        try:
         assert letter in ascii_lowercase
        except AssertionError:
            return False
    return True
            
def read_dictionary(filename, length):
    with open(filename, 'r') as f:
        words = set()
        f = f.readlines()
        for line in f:
            word = line.strip()
            if len(word) == length and word.islower() and clean_word(word):
                words.add(word)
        # words = [line.strip() for line in f if len(line.strip())==length and line.islower()]
    return words

class Node:
   def __init__(self, name, children):
      self.name = name
      self.children = children

   def __str__(self):
      return self.name

   def __repr__(self):
      return str(self)

   def get_children(self):
      return self.children

   def __eq__(self, other):
      """Override the default Equals behavior"""
      if isinstance(other, self.__class__):
         return self.name == other.name
      return NotImplemented

   def __ne__(self, other):
      """Define a non-equality test"""
      if isinstance(other, self.__class__):
         return not self.__eq__(other)
      return NotImplemented

   def __hash__(self):
      """Override the default hash behavior (that returns the id or the object)"""
      return hash(tuple(sorted(self.__dict__.items())))

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      global valid_words
      if valid_words == None or len(valid_words) != len(name):
         # We only need to examine words which have the same length as our word (self.name)
         valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
      self.name = name
      self.parent = parent
      self.depth = 10 #'''CHANGE'''
   def __str__(self):
      return self.name

   def heuristic(start, goal):
      if start == goal:
           return 0
      return 12
      return len([True for i in range(len(goal)) if goal[i] != start[i]]) -1
    

   def get_children(self):
      alphabets = list(ascii_lowercase)
      # all one letter mutations of the word
      child_words = [] # Your code here
      for i in range(len(self.name)):
          current = list(self.name)
          current_letter = current[i]
          for alpha in alphabets:
              if alpha != current_letter:
                current[i] = alpha
                rearranged_word = ''.join(current)
                if rearranged_word in valid_words:
                    child_words.append(WordGameNode(rearranged_word))
      return child_words

   def get_path(self):
      node = self
      while node.parent != None:
          path.append(node)
          node = node.parent
          
      path.append(node)
      return path

def a_star_search(start, goal):
   todo = [start]
   visited = set()
   num_searches = 0
   while len(todo) > 0:
      next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
      num_searches += 1

      if next == goal:
         return num_searches, next
      else:
         # Keep searching.
         visited.add(next) # Remember that we've been here

         # Add children to the todo list and update the score
         for child in next.get_children():
            print(child)
            if child not in visited and child not in todo:
               child.score = child.depth + child.heuristic(goal)  # score = g(n) + h(n)
               todo.append(child)

         # Sort the children by score (lowest better)
         todo.sort(key = lambda x : x.score)

   return num_searches, None # no route to goal

def main(args):
   if len(args) == 3:
      start_word = args[1]
      goal_word = args[2]
   else:
      start_word = input("Enter the start word: ")
      goal_word = input("Enter the goal word: ")
   assert len(start_word) == len(goal_word)

   # This reads the dictionary and updates the valid_words global variable for WordGameNode.
   read_dictionary("/etc/dictionaries-common/words", len(start_word))
   start = WordGameNode(start_word)
   goal = WordGameNode(goal_word)

   num_searches, end = a_star_search(start, goal) # Do the breadth first search
   print(num_searches)
   if end == None:
      print("There is no path from {0} to {1}".format(start, goal))
   else:
      print(end.get_path())

if __name__ == "__main__":
   main(sys.argv)


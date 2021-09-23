import sys
import os
import string
import re
import random
##   this code run in command line (1) without argument will internally test with embedded sample paragraph in below requirements, run "noarg.sh"
##                              or (2) usage: $0 <txt_filename> <page_size>, reads a text file, and align leftly+rightly text result to stdout. run "debug.sh"
##   code maintainer: Victor Huang, yahoo emailer id, huangxd. 
"""
REQUIREMENTS: text alignment, given any plain text, ask you left and right justify it!
    Write a program in Python, that can accept a paragraph string and page
width as parameters and return an array of left AND right justified
strings.
Note: No words should be broken
Submission Instructions:
Steps to execute your program (README)
A sample output
Unit tests are a big plus
•
Example:
Sample input values:
Paragraph = "This is a sample text but a complicated problem to be
solved, so we are adding more text to see that it actually works."
Page Width = 20
Output should look like this:
Array (1) = "This is a
sample"
Array [2] = "text but
a"
Array (3) = "complicated problem"
Array [4] = "to be solved, so
we"
Array [5] = "are adding more text"
Array (6] = "to see that
it"
Array [7] = "actually
works."

"""
## algorithm: pass 1. segment all 'pure words', and also their out, so "pure words" as paragraph will be segmented into word list=["Pure", " ", "words"]; 
##  --        pass 2. loop over all segmented list, pack them into current linked list, until next word will 'over flud' page width (==20, e.g.); which triggers
##                flushing out of link list, and headly starting next link list,  Calculate vacuum_size = page_max - linklist_footprint.
##            pass 3. vacuum_size = 0: continue.
##            pass 4. vacuum_size > linklist item_number, apparently inserting a space following each linklist item will be evenly alignment.
##            pass 5. vacuum_size < linked list item number, randomly select index, then add spaces in number of vacuum_size to linklist(excluding head & tail.  
##            pass 6. printing the page out (adding to page_list).
##            pass 7. when loop of pass2 over, write out all pages (to stdio or filename).
##  implementation: Using 3 class, LinkedList, Node, 
class LinkedList:

    class Node:
        
        #Class Invariant:
        #     self.data is an object of some data type
        #     self.next is a reference to another Node object, or None
        def __init__(self):
            self.data = None
            self.next = None
        
        #Pre:  self is a well defined Node object.
        #Post: return a string representation of this node and its
        #      neighbor.
        def __str__(self):
            return str(self.data) + " -> " + str(self.next)


    #Class Invariant:
    #     self.head is an attribute that either refers to
    #     a Node object, or None.
    def __init__(self):
        self.head = None

    #Pre:  data is some data to put into the linked list
    #Post: adds a node containing data to the front of the linked list
    def addFront(self, data):
        new_node = self.Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node

    #Pre:  data is some datatype
    #Post: adds a node containg data to the end of the linked list
    def append(self, data):
        if self.head == None:
            self.addFront(data)
        else:
            new_node = self.Node()
            new_node.data = data

            cursor = self.head
            
            while cursor.next != None:
                cursor = cursor.next
            
            cursor.next = new_node



    #Pre:  data is some data we want to remove from the linked list.
    #Post: Removes the first node containing data from the linked list.
    def delete(self, data):
        #find the node containing data
        previous = None
        pointer  = self.head

        while pointer.data != data:
            previous = pointer
            pointer  = pointer.next

        #Move previous node's next reference to the next node
        if previous == None:
            self.head = self.head.next
        else:
            previous.next = pointer.next


    #Pre:  index is an integer in the range of the size of the list
    #Post: returns the node at the specified index
    def get_node(self, index):
        cursor = self.head
        for j in range(index):
            cursor = cursor.next
        return cursor

    #Pre:  data is some data to add to the list.
    #      index is an integer, some location in the linked list to
    #      add data.
    #Post: Inserts a new node containing data somewhere in the linked
    #      list.
    def insert(self, data, index):
        if index == 0:
            self.addFront(data)
        else:
            new_node = self.Node()
            new_node.data = data
            #print("type(index)")
            #print(type(index))
            cursor = self.get_node(index - 1)
            new_node.next = cursor.next
            cursor.next = new_node
            
    #Pre:  index is an integer, some location in the linked list.
    #Post: returns the data from the node at the specified index.
    def get(self, index):
        cursor = self.get_node(index)
        return cursor.data
                
    #Pre:  self is a well defined linked list
    #Post: returns a string representation of this linked list.
    def __str__(self):
        return "head -> " + str(self.head)
    def geometry(self, lst):
        llen = 0
        house_size = 0
        cursor = self.head
            
        while cursor.next != None:
            house_size += len(cursor.data)
            llen += 1
            cursor = cursor.next

        house_size += len(cursor.data)
        llen += 1

        return llen, house_size

""" sniplet testing linked list and their use cases. 
if __name__ == "__main__":
    
    linked_list = LinkedList()
    for i in range(1, 11):
        linked_list.append(i)

    linked_list.insert(0, 0)
    print(linked_list)
    #head -> 0 -> 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None

    linked_list.delete(0)
    print(linked_list)
    #head -> 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None
"""
"""
# below from source:https://docs.python.org/3.7/library/re.html#re.split
>>> re.split('\W+', 'Words, words, words.')   # w + null
['Words', 'words', 'words', '']
>>> re.split('(\W+)', 'Words, words, words.') # w + p
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
    
"""
#class Page
class LR_JustifiedPage:
  def __init__(self, para, para_size, reg_str='(\W+\x27\W+)|(\W+)'):
        self.para = para
        self.para_size = para_size
        self.word_and_punt_list =  re.split(reg_str, para )
        self.wp_len = len(self.word_and_punt_list)     
        self.wp_ii = 0
        #print(self.word_and_punt_list) ## debug
        print("===============================================\n\n")
        self.page_list = []       
        self.raw_lines_constrained_by_para_size()
        #self.next_word_punct_ii()
        #self.print_page_list()
         
  def print_page_list(self):
      for page_ii in self.page_list:
          #print("type(page_ii)=")
          #print(type(page_ii))
          if page_ii is None:
              break
          print(page_ii+"\n")

    
# testing max well justified "grace number", rather than char-numbers /    
# each 'page' is a linked_list, in this case, word_num
# in implementation we constrain page justification by self.para_size, not word_num
# 

  def raw_lines_constrained_by_para_size(self ):
    wp_list = self.word_and_punt_list
    wp_len = len(wp_list)
    page_linkedList = []
    cur_linked_list = LinkedList()
    self.filled_size = filled_size = 0
    self.wp_ii = 0
    for ii in range(0, wp_len):
      if wp_list[ii] is None:
          continue
      if  filled_size + len(wp_list[ii]) < self.para_size:
        word_ii =   wp_list[ii]
        cur_linked_list.append(word_ii)
        filled_size += len(word_ii)
      else: # wrap up old page, and head_node current word  
        ret = wrap_a_page( cur_linked_list, filled_size, self.para_size)
        cur_linked_list = LinkedList()
        next_head = wp_list[ii]
        cur_linked_list.append(next_head) # head node it to new ll.
        page_linkedList.append( ret )  
        filled_size =  len(next_head)

        if ii < self.wp_len - 1 and wp_list[ii+1] is None:
            continue
        if ii < self.wp_len - 1 and (filled_size + len(wp_list[ii + 1]) > self.para_size):
          ret2 = wrap_a_page(cur_linked_list, filled_size, self.para_size)
          if ret2 is not None:
            self.page_list.append(ret2)
          cur_linked_list = LinkedList()
          next_head2 = wp_list[ii + 1]
          cur_linked_list.append(next_head2)  # head node it to new ll.
          filled_size = len(next_head2)
          ii += 1
    ret = wrap_a_page( cur_linked_list, filled_size, self.para_size)
    if ret is not None:
      page_linkedList.append( ret )
    # len, strip

    self.page_list = page_linkedList
    
# patch linkedList into a 'plain text' line    
def freeze_linkedList(linkedList):
  llen,house_size = linkedList.geometry(linkedList)
  freeze_len = 0
  #ret = linkedList.get_node(0).data.lstrip() # no leading spaces
  ret = linkedList.get_node(0).data # no leading spaces

  for ii in range(1,llen):
      raw = linkedList.get_node(ii).data
      ret += raw
  ret = ret.lstrip()
  print( ret )
  return ret, freeze_len
  # linkedList 
def evenly_packed_and_return_packed_size(linkedList):
  packed_size = 0
  llen,house_size = linkedList.geometry(linkedList)
  ret = ""
  for ii in range(1,llen-1): # no head and tail insert!
      item_ii = linkedList.get_node(ii)
      if item_ii == None or len(item_ii) == 0:
          continue
      if item_ii[0] not in string.punctuation:
        linkedList.insert(" ", ii)
        packed_size += 1 
  # linkedList
  return(packed_size)

# global function patch linked list, can be used out of class scope
def   random_pack_space_with_vacuum_size(linkedList, vacuum_size): 
  packed_size = 0
  llen,house_size = linkedList.geometry(linkedList)
  if llen < 2:
      return
  ret = ""
  
  # random.randint(0, 9)	Returns any random integer from 0 to 9
  while packed_size < vacuum_size:
      ii = random.randint(1,llen-1) # do not insert ' ' at head or tail
      item_ii = linkedList.get_node(ii)  #getnode() [ii]  # got item_ii randomly 
      data_ii = item_ii.data
      if data_ii is None:
          continue
      #print("ii="+str(ii)+",vacuum_size="+str(vacuum_size)+",llen="+str(llen))  
      if data_ii[0] not in string.punctuation:
        #print("ii="+str(ii)+",vacuum_size="+str(vacuum_size)+",llen="+str(llen))  
        linkedList.insert(" ", ii)
        packed_size += 1 
      if packed_size >= vacuum_size: 
          break
  return(packed_size)
  # linkedList 

# return a 'plain string' from linkedList          
def wrap_a_page( linkedList, filled_size, para_size):
  ret = ""  
  vacuum_size = para_size - filled_size # some vacuums to fill with single space
  if vacuum_size == 0 :
      ret = freeze_linkedList(linkedList)
  elif vacuum_size > para_size:
     packed_size = evenly_packed_and_return_packed_size(linkedList)     
     vacuum_size -= packed_size
     wrap_a_page( linkedList, vacuum_size, para_size) # recursive, reduced packed_size
  else :
     filled_size2 = random_pack_space_with_vacuum_size(linkedList, vacuum_size) 
     ret,fr_len = freeze_linkedList(linkedList)
  return ret  

# it default to sample paragraph from tester without command line argument, e.g.
#   -- refer to noargs.sh
# but can be used in automatic testing via command line arguments , with batch text filename,
#   -- refer to debug.sh
#  -- with automatic variable page_len;
#  -- with different parsing format in list=["\w+", "\(W+)"] etc for experiments     
if __name__=="__main__":
  argv=sys.argv
  usage = "Usage: \"+argv[0]\" txt_filename[.txt] <page_len> <parsed_reg_format>"
  usage02 = "  e.g.:  \"+argv[0]\" sample.txt 20 \W+"
  if len(argv) < 4:
    print(usage)
    print(usage02)
    #sys.exit(1)
    para = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
    #para = "complicated problem to be solved, so we are adding more text to see that it actually works."
    page = LR_JustifiedPage(para, 20)
    sys.exit(0)

page = LR_JustifiedPage(para, 21)
para = open( sys.argv[1], "rt" ).read()
#page = LR_JustifiedPage(para, int(sys.argv[2]), sys.argv[3] ) 
page = LR_JustifiedPage(para, int(sys.argv[2]) ) 



"""
memo:
build Markov Chain data structures;
while( more words to generate ) {
   generate next word;
   if( word is short enough to fit on current output line )
      add word and trailing space(s) to the line;
         // Two spaces if it is the end of a sentence.  See below.
   else {
      add spaces to justify the line; // details in phase 3
      print the line;
      clear the linked list;
      add the word and trailing spaces to the line;
   }
}
if( output line is not emtpy )
   print output line;

""" 

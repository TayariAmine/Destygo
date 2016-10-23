# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 23:39:48 2016

@author: Tayari
"""

import sys
import inspect

class Node:
    def __init__(self, val):
        self.left = None # is a Node
        self.right = None # is a Node
        self.value = val

# ABR : 
# left.val <= val <= righ.val
class Tree:
    
  def __init__(self, node):
      self.root = node
      
  def add(self, val):
      if self.root == None :
          self.root = Node(val)
      else:
          self.insert(val)

  def insert(self, val):
      if self.root == None:
          	self.setRoot(Node(val))
      else:
            currentRoot = self.root
            while(True):
                if val <= currentRoot.value:
                    if currentRoot.left != None:
                        currentRoot = currentRoot.left
                    else:
                     	currentRoot.left = Node(val)
                        break
                else:
                    if currentRoot.right != None:
                       currentRoot = currentRoot.right 
                    else:
                        currentRoot.right = Node(val)
                        break
          
  def run(self, val):
      return self.find(val)

  def find(self, val):
        currentRoot = self.root      
        while ((currentRoot is not None) and (currentRoot.value != val)):
            if val <= currentRoot.value:
                currentRoot = currentRoot.left
            else:
                currentRoot = currentRoot.right
        if currentRoot == None:
                return False
        else :
            return True
            
  def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)
      

# Creation de l'arbre et l'ajout des noeuds 
if __name__ == '__main__':
    T = Tree(Node(1))
    toadd = [7,8,4,9,5,1,2]
    for s in toadd:
        T.add(s)
        
#verification de la presence de 11 dans l'arbre
    print T.run(11)
    
#verification de la presence de 11 dans l'arbre   
    print T.get_classes()
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:17:57 2016

@author: Tayari
"""


import sys
import inspect

class Sum : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       t=0
       l=self.n+1
       for i in range(l):
           if (i%3)==0 or (i%5)==0:
               t+=i
       return t
   
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)
      
      
if __name__ == '__main__':  

# Calcul et affichage de la somme pour n=30      
    sum = Sum(30)
    print sum.run()

# Affichage de la liste des classes 
    print sum.get_classes()
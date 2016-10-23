# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 19:33:22 2016

@author: Tayari
"""

import sys
import inspect
from math import sqrt

## Méthode 1:  --------------------------------------------------------------

class Loop : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       a,b = 1,1
       l=self.n+1
       for i in range(l):
           a,b = b,a+b
       return a-1
     
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)

# Calcul et affichage pour n=30 
if __name__ == '__main__':
    loop = Loop(30)
    print loop.run()

# Affichage de la liste des classes 
    print loop.get_classes()    
    

## Méthode 2:  --------------------------------------------------------------
"""
Dans cette méthode, j'ai utilisé la formule mathématique réduite de Fn

"""
class Expr_red : 
   
   def  __init__(self,n):
        self.n=n
   
   def run(self):
       l=self.n+2
       return (((1+sqrt(5))**l-(1-sqrt(5))**l)/(2**l*sqrt(5)))-1
   
   def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)
      
# Calcul et affichage pour n=30 
if __name__ == '__main__':
    Expr_red = Expr_red(30)
    print Expr_red.run()
    
# Affichage de la liste des classes 
    print Expr_red.get_classes()   
 
 
 
## Méthode 3: --------------------------------------------------------------
"""
Dans cette partie, j'ai utilisé la forme récursive de la suite de Fibonacci 
  
"""
class Recursive :
    
    def  __init__(self,n):
        self.n=n
        
    def run(self):
       return self.fibR(self.n+2)-1 #
       
    def fibR(self,i):
       if i==0: 
           return 0
       elif i==1:
           return 1
       return self.fibR(i-1)+self.fibR(i-2)
       
    def get_classes(self):
      self.current_module = sys.modules[__name__]
      return inspect.getmembers(sys.modules[__name__], inspect.isclass)
 
# Calcul et affichage pour n=30 
if __name__ == '__main__':
    Recursive = Recursive(30)
    print Recursive.run()
    
# Affichage de la liste des classes 
    print Recursive.get_classes()
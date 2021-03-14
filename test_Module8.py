import itertools
##Create a manual list 
x = [1,2,3,4,5]
print (x)

import unittest
class ListTest(unittest.TestCase):
  def CREATE_LIST(self):
    assert x == ("1,2,3,4,5")

if __name__ == '__main__':
 unittest.main()

print ("\n")

##copy list
import copy
y = copy.copy(x)
print(y)

import unittest
class ListCopy(unittest.TestCase):
  def CREATE_COPY(self):
    assert y == ("1,2,3,4,5")

if __name__ == '__main__':
 unittest.main()

print ("\n")

##re-copy list
z=copy.copy(x)
print(z[2])

import unittest
class ListReCopy(unittest.TestCase):
  def CREATE_RECOPY(self):
    assert z == ("3")

if __name__ == '__main__':
 unittest.main()


print ("\n")


import itertools
for i in itertools.count(10, 5):  
    if i == 35:  
        break
    else:  
        print(i, end =" ")

import unittest
class ListCount(unittest.TestCase):
  def CREATE_COUNT(self):
    assert i == ("10, 15, 20 ,25, 30")

if __name__ == '__main__':
 unittest.main()


print ("\n")

##infinite iterator
 
print ("\n")

##itertools.cycle
import itertools
count = 0
  
# for in loop 
for i in itertools.cycle('LOOP'): 
    if count > 19: 
        break
    else: 
        print(i, end = " ") 
        count += 1 

import unittest
class ListCycle(unittest.TestCase):
  def CREATE_CYCLE(self):
    assert i == ("LOOPLOOPLOOPLOOPLOOP")

if __name__ == '__main__':
 unittest.main()

print ("\n")

##itertools.repeat
import itertools  
    
# using repeat() to repeatedly print number  
print (list(itertools.repeat('REPEAT', 10))) 

import unittest
class ListRepeat(unittest.TestCase):
  def CREATE_REPEAT(self):
    assert list == ("REPEAT, REPEAT, REPEAT, REPEAT, REPEAT, REPEAT, REPEAT, REPEAT, REPEAT, REPEAT")

if __name__ == '__main__':
 unittest.main()

'''import module #import module as m(alias) 
print(module.likes)
print(module.addlikes())
print(module.addlikes())
print(module.addcomments("Good"))

import module  as m#import module as m(alias) 
print(m.likes)
print(m.addlikes())
print(m.addlikes())
print(m.addcomments("Good"))

from module import likes,comments,addlikes,addcomments
print(likes)
print(addlikes())
print(addlikes())
print(addcomments("Good"))

from module import *
print(likes)
print(addlikes())
print(addlikes())
print(addcomments("Good"))
'''
from module import *
print(add(4,5))
print(subtract(5,4))
print(multiply(5,8))
print(divide(10,5))
print(modulus(3,2))

from module import add,subtract,multiply,divide,modulus
print(add(4,5))
print(subtract(5,4))
print(multiply(5,8))
print(divide(10,5))
print(modulus(3,2))

import module as m
print(m.add(4,5))
print(m.subtract(5,4))
print(m.multiply(5,8))
print(m.divide(10,5))
print(m.modulus(3,2))

import module
print(module.add(4,5))
print(module.subtract(5,4))
print(module.multiply(5,8))
print(module.divide(10,5))
print(module.modulus(3,2))
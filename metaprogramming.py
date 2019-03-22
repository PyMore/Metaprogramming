#!/usr/bin/env python
# coding: utf-8

# The arguments when invoking type are the name of the class, a list of base classes, and a dictionary giving the namespace for the class (all the fields and methods). So the equivalent of:
# 
# class C: pass
# c = type('C',(),{})

# In[13]:


def homdy(self,you):
    print(f'Homdy {you}')

MyList  = type('MyList',(list,),dict(x=42,homdy=homdy))

test = MyList()
test.homdy('hey')
test.append('Camembert')
print(test)
print(test.x)
print(test.__class__)


# Metaclass programming looks like this

# In[49]:



class SimpleMetaClass(type):
    """ Simple Meta Class"""
    def __init__(cls, name, bases, nmspc):
        super(SimpleMetaClass,cls).__init__(name, bases, nmspc)
        cls.uses_metaclass = lambda cls : "Yes!"        

class Demo(metaclass=SimpleMetaClass):
    """ Demo Class """
    def foot(self): pass
    
    
d = Demo()
print(d.uses_metaclass())
#d.uses_meta()


# 

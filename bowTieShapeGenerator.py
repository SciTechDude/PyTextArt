
# Author: Anil Mandra 
#
# (c) 2017
# Modified By : Anil Mandra anil.mandra@yahoo.com
#
#License: MIT

from __future__ import print_function
from itertools import islice, chain

class BowTie(object):
    def __init__(self, size=5, fill_value = '*', empty_value = ' ', hollow = None):
        self.size = size
        self.fill_value = fill_value
        self.empty_value = empty_value
        self.hollow = hollow
        

    def  create_shape(self):
        ''' creates shape as per input values and returns list of list of values'''
        face = [self.fill_value,self.empty_value] * ((self.size*2) - 1)
        rows = list(chain(range(self.size),reversed(range(self.size-1))))
        for i in rows:
            f = ''.join(islice(face, i, (i*2)+1))            
            if not self.hollow:
                s = ''.join(chain(f , [self.empty_value * (self.size - (i + 1))]))                
            else:
                self.empty_value = ' '
                l = [self.fill_value if idx == 0 or  idx == len(f)-1 else self.empty_value for idx,m in enumerate(f)]
                s = ''.join(chain(l, [self.empty_value * (self.size - (i + 1))]))
                
            yield ''.join(s + s[::-1][1:])

    def print_shape(self):
        ''' print given list of list of values'''
        for i in self.create_shape():            
            print(i)


#example use 1
BowTie(size=5, fill_value = '*', empty_value = '.', hollow = False).print_shape()

#example use 1
BowTie(size=7, fill_value = '#', empty_value = ' ', hollow = False).print_shape()

#example use 2
BowTie(size=10, fill_value = '+', empty_value = '.', hollow = True).print_shape()

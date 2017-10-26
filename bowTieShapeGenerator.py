# Author: Anil Mandra 
#
# (c) 2017
# Modified By : Anil Mandra anil.mandra@yahoo.com
#
#License: MIT

from __future__ import print_function

class BowTie(object):
    def __init__(self, size=5, fill_value = '*', empty_value = ' '):
        self.size = size
        self.fill_value = fill_value
        self.empty_value = empty_value

    def  create_shape(self):
        ''' creates shape as per input values and returns list of list of values'''
        star = self.fill_value
        dot = self.empty_value
        m = (self.size * 2) - 1 #Get center row
        
        #get  top half list
        th = []
        for idx,k in enumerate(xrange(1,self.size+1)): #run through 1 - size
            row = idx + 1
            tmplst = []
            if row % 2 != 0:
                tmplst.append(i for i in xrange(1,row + 1) if i % 2 != 0)
                tmplst.append(i for i in xrange(m, m-row, -1) if i % 2 != 0)
            else:
                tmplst.append(i for i in xrange(1,row + 1) if i % 2 == 0)
                tmplst.append(i for i in xrange(m, m-row, -1) if i % 2 == 0)
                
            #append each row value to  top half list.
            th.append(sorted(set([j for i in tmplst for j in i])))

        #create palindrome of top half which is our bottom half 
        th = th + th[len(th) -2::-1]

        def get_list(bound = self.size, alist = []):
            ''' expects upper bound and an integer list
            returns a list of fill_values '''        
            tmp_list = []            
            for i in xrange(1,bound + 1):
                tmp_list.append(star if i in alist else dot)
            return tmp_list
             
        #create list of * and blanks or as per fill and empty value
        row_values = [get_list(bound = m, alist = i) for i in th]
        return row_values

    def print_shape(self):
        ''' print given list of list of values'''
        for i in self.create_shape():
            print(' '.join(i))

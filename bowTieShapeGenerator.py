import getopt, sys

def bowTie(n = 5):
    ''' expect n as integer
        returns nothing
         Creates bow tie pattern of length n '''
    
    def get_list(bound, alist):
        ''' expects upper bound and an integer list
            returns a list of star '''
        tmp_list = []
        for i in xrange(1,bound + 1):
            tmp_list.append(star if i in alist else dot)
        return tmp_list

    star = "*"
    dot = " "
    
    m = (n * 2) - 1 #Get center row

    #get  top half list
    th = []
    for idx,k in enumerate(xrange(1,n+1)): #run through 1 - n
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
         
    #create list of * and blanks
    final = [get_list(m, i) for i in th]

    #Print BowTie
    for i in final:
        print ' '.join(i)

def usage():
    ''' display usage '''
    print "Error: You need to supply an integer number"
    
def main():
    ''' Expects nothing
        Returns nothing
        Gets user input and executes bowtie function '''
    py_version = sys.version_info[0]
    if py_version <=2:
        try:
            num = int(raw_input("Enter BowTie Row Number:"))
            bowTie(num)
        except ValueError:
            usage()
    else:
        try:
            num = int(input("Enter BowTie Row Number:"))
            bowTie(num)
        except ValueError:
            usage()

if __name__=='__main__':
    main()
        

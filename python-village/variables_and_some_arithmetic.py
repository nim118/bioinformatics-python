# Problem Url : http://rosalind.info/problems/ini2/
# Code to print Addition of square root of 2 numbers.
import sys
class Variable:

    #Function for addition of square root of 2 numbers.
    def addition(self, a, b):
        return a**2 + b**2

#Driver Code.
if __name__ == "__main__":

    # Code to read data from the file
    try:
        f = open(sys.argv[1], "r")
        f_data             = f.readline()
        first_line         = f_data.strip().split(" ")
        a                  = int(first_line[0])
        b                  = int(first_line[1])
    except:
        print "Invalid File"

    #Create Object of class
    obj = Variable();
    c = obj.addition(a, b)
    
    print c
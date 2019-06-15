#problem url : http://rosalind.info/problems/ini4/
#Code to print the sum of all odd integers from a through b, inclusively.
#Importing sys to take the command line argument.
import sys
class Loop:

        def getSumOfOddNumbers(self, a, b):
                adition = 0
                for i in range(a, b+1):
                        if i % 2 == 1:
                                adition = adition + i
                return adition


#Driver Code.
if __name__ == "__main__":
# Code to read data from the file
    try:
        f                  = open(sys.argv[1], "r")
        f_data             = f.readline()
        first_line         = f_data.strip().split(" ")
        a                  = int(first_line[0])
        b                  = int(first_line[1])
    except:
        print ("Invalid File")

#Create Object of class.
obj = Loop();
c   = obj.getSumOfOddNumbers(a, b)
print (c)
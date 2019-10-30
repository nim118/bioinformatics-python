# http://rosalind.info/problems/2sum/

# Class Code

class Twosum:

    #Init function to declare class variables.
        
    #Function to find 2 sum 
    def find2Sum(self, arr):

        for i in range(0, len(arr)): 
            arr[i] = int(arr[i]) 

        found = "-1"
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if (arr[i] == -(arr[j])):
                    found = ""+str(i + 1)+" "+str(j+1)
                continue

        print found     

# Driver Code
if __name__ == "__main__":
    
    #code to read data from the file. 
    f = open("rosalind_2sum.txt", "r")
    f_data           = f.readlines()
    first_line       = f_data.pop(0).strip().split(" ")

    t = Twosum();

    for arr in f_data:
        t.find2Sum(arr.strip().split(" "))
#problem url : http://rosalind.info/problems/ini5/
f = open('input.txt', 'r')
count = 1
for line in f:
	if(count%2 == 0):
		print (line.strip())
	count = count + 1


f.close()
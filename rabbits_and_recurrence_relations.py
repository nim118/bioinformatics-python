n = 35
#n is number of months
#fn = fn-1 + fn-2*k
#Positive integers n≤40 and k≤5.

k = 4
#k is number of rabiits pairs reproduced by every pair 

serise = [1, 1]
count = 1

while count < n-1:
	serise.append(serise[count] + serise[count-1] * k)
	count = count + 1


print serise

print serise[len(serise) - 1]

print len(serise)
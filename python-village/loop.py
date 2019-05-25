#problem url : http://rosalind.info/problems/ini4/
a = 4479;
b = 9464;
adition = 0;

for i in range(a, b+1):
    if i % 2 == 1:
        adition = adition + i;    


print (adition);

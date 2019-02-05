f = open('output.txt', 'w')

some_kind_of_list = ["I will live my dream one day", 1, 24]

for item in some_kind_of_list:
	f.write(str(item) + '\n')


f.close()
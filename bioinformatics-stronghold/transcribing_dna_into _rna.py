# Problem Url :  http://rosalind.info/problems/rna/
dna = 'TCGCGAAAGCGGAAAAATAAACTTAGGCGGTTATGAAAGCTCCCCATGTCGCCGAGTGATACATGTATGACGGCCCTCACGATGCCTGAAACCCAGCCTGTGAGCCATGGTTTAATACCACTATGGAGCGCGATTCCCCCTCTCCGGCTGTTTACAGGTAATTCTCAATAATAGACGAAAGTGTAGCTCCTTTAGCCTCTACGGGGTGTCCGAATCAGCTAAGGGAACGGTAGGTTGGTGAAATGCGAAATATCAATCAGTATTCGTTGGTGTCTCCCCGTAAAACAGATGTAGTCTATTCTGGTCTTCGTCGATCTCAGGGGAGATATACTTGTGCCCGCCCCCCGCTTACAGGGGTACGCGTCACGACACAACCGAAGTGCGCCGCCTAAAACTGTACCCGATAGAAAGTTAGTCGCAGGTACCCGACTGTGAGACCCAACAGATGATCACTTCACGCCTTCATTCATAACATCCCCCCCGATGTTCTTCGGGTGAAGCGGGGTCAAGGACCTACCTACAGACCAGCTTGTCCCGGGCACACACATGCTCAGAAACGGTCAAAGATGGCCTGCTTGGCAGTCGCGCGAATACGTTACCACGCAACATCCCCCGGGAGCATATGACTCCCCGGTAGAGGCCAGGTGAGTATCAAGAGGTTATGGAAGAATTATGGATAGCTCCGGTTGGGATGAGCAAGTGTTAGCCGGGGCAGCAAAGCCAGCATGATTAAATCCTCTAGGTATAGGGTGTGCGCTGTTAAGCCCTCAAGGGAATAGCCTGCTTCACTACTTACTGGGTGGGTTCCCAGAGCTATGTCTGTAACCGATAGCTCTTTGGTTCGCTTCCCTTATTTGGACGTCGACACATCCCTATCTGGTCCACGGATCCCAGAATGGGGATCAACAGGATGTATTCA'
rna = ''

for letter in dna:
	if (letter == 'T'):
		letter = 'U'
	rna = rna + letter


print (rna)
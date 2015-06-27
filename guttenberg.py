

#reading
file1 =open('book.txt','r')
for line in file1:
	print line


#counting words
file1 =open('book.txt','r+')
wordcount={'great','good','adventure','the','while'}
	for word in file1.read().split():
		if word not in wordcount:
			wordcount[word]=1
		else:
			wordcount[word] +=1
	for k,v in wordcount.items():
		print k,v


#appending
file2 = open('book.txt', 'a')
	try:
    	byte = f.read(1)
    	while byte != "":
        # Do stuff with byte
        byte = f.read(1)
	finally:
   		f.close()

#reader program
def reader('filename'):
	file1=open('filename','r')
	#either
	for line in file1:
		print line
	#or
	file1.readlines()





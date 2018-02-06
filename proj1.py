#Part 2 (2.5 marks)
#boolean_query
#Write a program that performs boolean queries on the index.

#The command line arguments should be the path to the index followed by a boolean query
#Usage:
#~>./boolean_query [index file location] [query]
#Queries consist of:
#single terms
#phrases, consisting of two or more terms enclosed in double quotes (")
#Boolean expressions involving terms, phrases, or sub-queries connected with AND, OR and NOT operators
#Sub-queries are Boolean expressions enclosed in parenthesis (()
#Operator precedence should be handled as described here https://en.wikipedia.org/wiki/Logical_connective
#Your program should print the id of each document that satisfies the query, with one id per line.
#The order of the documents ids in the answer is not important for boolean queries.
#If an ill-defined query is provided (e.g., term AND) your program should print an error message and no other output.
#For example, the query dictionary AND love should return documents 101 and 1712 (each on a different line) while the query (dictionary AND love) OR ("harry potter" AND azkaban) should return documents 101, 690, 692, 694, and 1712.


#Part 4 (2.5 marks)
#zone_scoring
#Write a program that does weighted zone scoring (Chapter 6) and returns the document ids of the top k documents ranked according to equation 6.2 for a Boolean query q, provided as a command line argument.

#Queries should be as in Part 2 above. (Hint: reuse your code!)

#Usage and Parameters:

#./create_zone_index [document dir] [index dir]
#./zone_scorer [index dir] [k] [g] [q]
#All parameters are required. Your create_zone_index program will not be graded, but must be submitted.

#Note that the query may span multiple command line arguments. Hint: form the query by concatenating in a single string all command line arguments to the program, after the parameter g, adding white spaces between tokens.

#Note also that you are not asked to learn the optimal value of g. Assume it is a real number between 0 and 1.

#Output:

#doc_id1 score_1
#doc_id2 score_2
#...
#doc_idk score_k
#Where score_1 >= score_2 >= … >= score_k

#There should be two zones: title and body. The body is the content of the file, while the title is encoded in the file name. IMPORTANT: when tokenizing the titles, make sure to separate words connected by _ (e.g., 101_Dalmatians_1996 is tokenized into 101 Dalmatians and 1996).


import sys
import re
import os

takein = sys.stdin

def terms():
	#pat = r'<(article|inproceedings) key=\"([\w\/-]+)\">(.*?)</\1>'
	auth = r'<author>(.*?)</author>'
	titl = r'<title>(.*?)</title>'
	jour = r'<(journal|booktitle|publisher)>(.*?)</\1>'
	year = r'<year>(.*?)</year>'
    docid = r'doc_(.*?)_' #new not sure it works yet
	try:
		os.remove('index.txt')
		os.remove('years.txt')
		os.remove('recs.txt')
	except:
		pass

	file=open('index.txt','w')

	f=open(x'.txt','r') #new not sure it works
	fi=open('recs.txt','w')

	for line in takein:
		m = re.search(pat, line)
		if m:
			key = m.group(2)
			inner = m.group(3)
			m2 = re.findall(auth, inner)
			m3 = re.findall(titl, inner)
			m4 = re.findall(jour, inner)
			m5 = re.findall(year, inner)
			lin = "{}:{}".format(key,line)  
			fi.write(lin)

			for t in m3:
				new = re.split("\W", t)
				for i in new:
					if len(i) > 2:
						i = i.lower()
						line = "t-{}:{}\n".format(i, key)
						file.write(line)

			for o in m4:
				o = o[1]
				new = re.split("\W", o)
				for i in new:
					if len(i) > 2:
						i = i.lower()
						line = "o-{}:{}\n".format(i, key)
						file.write(line)

			for a in m2:
				new = re.split("\W", a)
				for i in new:
					if len(i) > 2:
						i = i.lower()
						line = "a-{}:{}\n".format(i, key)
						file.write(line)

			for t in m5:
				new = re.split("\W", t)
				for i in new:
					if len(i) > 2:
						i = i.lower()
						line = "{}:{}\n".format(i, key)
						f.write(line)
	file.close()
	f.close()
	fi.close()
terms()

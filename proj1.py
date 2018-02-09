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
import argparse
from collections import defaultdict
#import nltk 
#nltk.download('punkt')
takein = sys.stdin
#ZONE SCORING

#for arg in sys.argv:
    #print(arg)

def create_zone_index(doc_dir, ind_dir):
    print("create_zone_index selected")
    index_file = open(ind_dir+'/index.txt', 'w')
    for filename in os.listdir(doc_dir):
        file_path = doc_dir+'/'+filename
        doc_id =os.path.splitext(filename)[0]
        doc_id = doc_id.split('_')
        docnum = doc_id[1]
        title = doc_id[2:]
        print(title)
        file = open(file_path, 'r')
        index = idict(list)
        for words in file:
            
            word = words.split(" ")

            for i, tokens in enumerate(word):
                index2 = idict(list)
                doc_pos = "{}:{},".format(  docnum, i,)
                index2[tokens].append(doc_pos)
        index.update(index2)
        print(index)
        line1 = "{}".format(index)
        index_file.write(line1)

        file.close()
    #index_string = "{}".format(index_file)
    #for words in index_file:

    index_file.close()
 




def print_index (data):
    index_file = open(ind_dir+'/index.txt', 'r')
    print(index_file)
    index_file.close()





   # pat = r'<(article|inproceedings) key=\"([\w\/-]+)\">(.*?)</\1>'
    
def zone_scorer(dir, k, g, q):
    print("zone scorer selected")

def main():
    what_to_do =sys.argv[1]
    if what_to_do == './create_zone_index':
        create_zone_index(sys.argv[2], sys.argv[3])
    elif  what_to_do == './print_index':
        print_index(sys.argv[2])
    elif what_to_do == './zone_scorer':
        zone_scorer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("error: command line arguments ")
    


if __name__ == "__main__":
    main()

import sys
import re
import os

takein = sys.stdin

def index_it(): #dir - directory to be indexed
    #try:
        #os.remove('index.txt')
        #open directory - list all files in dir - open each file and index words - skip if cant read and print error
    #except:
        #pass    #for i #for #of docs in directory
    #    x = 'doc_'+i+'_' #name of txt file
    pat = r'<=\"([\w\/-]+)\">(.*?)</\1>'
    file1 = open('index.txt', 'a')
    file2 = open('index.txt', 'r')
    file = open('hash.txt', 'r')

    index_already = file2.read()
    #doc_id = 'doc_9_101_dalmations_1996.txt'

    print(os.path.splitext("doc_9_101_dalmations_1996.txt")[0])
    doc_id =os.path.splitext("doc_9_101_dalmations_1996.txt")[0]

    doc_id = doc_id.split('_')
    docnum = doc_id[1]
    title = doc_id[2:]
    print(docnum)
    print(title)
    for line in takein:
		m = re.search(pat, line)
        if m:
    for line in file:
        line = line.strip()
        line = line.split(" ")

        for i in range(len(line)):
            print(line[i]) #word
            index_already = file2.read()
            
            if line[i] not in index_already:
                word = "{}\t".format(line[i]) #create it
                file1.write(word)
                print('create new index entry')
            else:
                print('append to index entry')
            num = " {}".format(docnum) #current doc id
            file1.write(num)
            word = " :{}".format(i) #positional index
            file1.write(word)
            word = ";" #create it
            file1.write(word)
            word = "\n" #new line need for loop before this? or insert new instances before this
            file1.write(word)
    #word = 'its red'
    #wordlist = word.split(' ') #split at the white space, returns a list of strings
    #wordlist[0] #returns 'its'
    #wordlist[1] #returns 'red'
    file.close()
    file1.close()
    file2.close()

#def print_index(directory)   
    #check if index

    #print index
def main():
    #what_to_do =sys.argv[1]
    #if what_to_do == 'print_index'
        #print_index(sys.argv[2])
    index_it()


if __name__ == "__main__":
    main()

import sys
import re
import os

takein = sys.stdin

def terms():
	pat = r'<(article|inproceedings) key=\"([\w\/-]+)\">(.*?)</\1>'
	auth = r'<author>(.*?)</author>'
	titl = r'<title>(.*?)</title>'
	jour = r'<(journal|booktitle|publisher)>(.*?)</\1>'
	year = r'<year>(.*?)</year>'
	try:
		os.remove('terms.txt')
		os.remove('years.txt')
		os.remove('recs.txt')
	except:
		pass

	file=open('terms.txt','w')
	f=open('years.txt','w')
	fi=open('recs.txt','w')

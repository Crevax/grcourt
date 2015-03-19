#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import csv, os, re, urllib2, urllib, requests, cookielib, mechanize, robotparser, time, random, string, sys, sqlite3
from bs4 import BeautifulSoup

print "We are in the right spot"
os.system("del criminal_out.csv")

#Our source
gr_url = 'http://grcourt.org/CourtPayments/loadCase.do?caseSequence=1'
nmax = 891429

#Get Cookie
r = requests.get('http://grcourt.org/CourtPayments/loadCase.do?caseSequence=1')
headers = r.headers['set-cookie']
print headers

#Initialize opener add cookie
opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', headers))

count = 1


while count < nmax:
	print 'On Case #:', count
	criminal_out = open(str(count) +'.html', 'ab')
	#Request Page
	f = opener.open('http://grcourt.org/CourtPayments/loadCase.do?caseSequence=' + str(count))
	bsoup = BeautifulSoup(f.read())
	#global problems
	#problems = []
	#Storing the first b tag inside body to data_ccsort 
	data_ccsort = bsoup.body.b
	
	#If statement that sorts out civil cases 
	if data_ccsort.string == u'Civil Case View':
		print "Civil Case Continue..."
		count +=1
		print "ZZZZZZZ..."
		time.sleep(2.5)
	elif data_ccsort.string == 'Unable to load case data':
		print "Unable to load case data"
		count +=1
		print "ZZZZZZZ..."
		time.sleep(2.5)
	else:
		print "Criminal Case"
		
		criminal_out.write(str(bsoup))
		
		count += 1
		print count
		criminal_out.close()
		time.sleep(2.5)
#print problems, "Problem child?"


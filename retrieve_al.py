#!/usr/bin/env python
import urllib2
import pymarc
import sys

##alephno=sys.argv[1]
alephno = "003477310"
##FIGURE THIS OUT
## if alephno == null
##    print "no alephno found"
## else
afile = urllib2.urlopen('http://library.emory.edu/cgi-bin/get_bibrecord?doc_id=' + str(alephno))
print afile.read()
##def get_auth_ids:
##    tags = (100,110,111,130,240,600,610,611,630,650,651,655,700,710,711,730,800,810,811,830)
##    extract = file[]
##    reader = marc.reader(file)
##    for record in reader
##    
##    if record.tag in tags:
##      if record []['0']:
##          print alephno, record.tag, ['a'], ['0']
##          extract.append(alephno, tag, ['a'], ['0'])
##      else
##          print alephno, tag, ['a'],


def readtags():

    reader = marc.reader(open(afile))
    fields = afile.getFields('100', '110', '111', '130', '240', '600', '610', '611', '630', '650', '651', '655', '700',
                              '710', '711', '730', '800', '810', '811', '830')
    print fields    
###  for afield in authfields

###        if afield.

pymarc.map_xml(readtags, afile)

    
    
    






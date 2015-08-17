#!/usr/bin/env python
__author__ = 'Laura Akerman'
import urllib2
import pymarc
from pymarc import Record, Field, XmlHandler
import sys

# inputFileName = sys.argv[1]
# outputFileName = sys.argv[2]
class Getrecords:
    def __init__(self):
        pass

    def getbibs(inpufile):
        inputFile = open("alephnos.txt", "r")
        inputFileLines = inputFile.readlines()
        inputFile.close()
        if len(inputFileLines) == 0:
            print "No input data!"
            sys.exit()

        my_marcs = []

        # If there's a way to parse a single XML record from each Aleph call/datastream, I haven't found it yet...
        # parse_xml_to_array works so I just use the first instance and append it to a file of record objects for now

        for line in inputFileLines:
            afile = urllib2.urlopen('http://library.emory.edu/cgi-bin/get_bibrecord?doc_id=' + str(line))
            my_array = pymarc.parse_xml_to_array(afile)
            my_marcs.append(my_array[0])

        print my_marcs
        my_tags = ['100', '110', '111', '130', '240', '600', '610', '611', '630', '650', '651', '655', '700', '710', '711',
           '730', '800', '810', '811', '830']
        extract = []

        # This needs to be fancier and only select subfield zeros that begin with "EMU"....  later...
        for marc_rec in my_marcs:     # print (marc_rec)
            my_fields = marc_rec.get_fields()
            a_number = marc_rec.get_fields('001')[0].value()

        for field in my_fields:
            if field.tag in my_tags:
                if len(field.get_subfields('0')) > 0:
                    package = []
                    package.append(a_number)
                    s_zeros = field.get_subfields('0')
                    for subfld in s_zeros:
                        package.append(subfld)
                    extract.append(package)
                    # print (extract)
                    return my_marcs, extract
                if len(extract) == 0:
                    print "No auth data for these records!"
                    sys.exit()

    def getauths(extract):
        my_auths = []
        for line in extract:
            authfile = urllib2.urlopen('http://library.emory.edu/cgi-bin/get_authrecord?auth_id=' + str(line[1]))
            my_autharray = pymarc.parse_xml_to_array(authfile)
            my_auths.append(my_autharray[0])
            return my_auths




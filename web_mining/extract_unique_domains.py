#!/usr/bin/python2

import argparse
from urlparse import urlparse

def GetUrlDomain(url):
   parsed = urlparse(url)
   return '{}://{}'.format(parsed[0], parsed[1])

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)
cmdlineArgs = vars(parser.parse_args())

filepath = str(cmdlineArgs['file'])

file = open(filepath, 'r')

domainSet = set()

for line in file:
   domainSet.add(GetUrlDomain(line.strip()))

for item in sorted(domainSet):
   print item

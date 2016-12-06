import argparse
import urllib2

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)
parser.add_argument('-u', dest='url', type=str, required=True)
cmdlineArgs = vars(parser.parse_args())

filepath = str(cmdlineArgs['file'])
url = str(cmdlineArgs['url'])

file = open(filepath, 'r')

urlOpener = urllib2.build_opener()

for line in file:
   userAgent = line.strip()
   urlOpener.addheaders = [('User-Agent', userAgent)]
   try:
      resp = urllib2.urlopen(url)
   except urllib2.URLError, e:
      if hasattr(e, 'reason'):
         print 'User-Agent: %s\nFailed with error: %s' % userAgent, e.reason
      elif hasattr(e, 'code'):
         print 'User-Agent: %s\nFailed with error: %s' % userAgent, e.code

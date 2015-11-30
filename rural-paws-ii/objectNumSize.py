#script to arse the HAR file and return detailed timing information about page load time process
#written by hassan hamdoun , hassan@erg.abdn.ac.uk, for rural paws project, 20/01/2014

#from__future__import print_function 
import fileinput
import json 
import os
import csv 
import re
import linecache
import string
from string import digits
import dateutil.parser as dparser
from datetime import timedelta
#from nltk.tokenize import RegexpTokenizer
import string 
import sys
import json
import time
import collections
from getopt import getopt
from textwrap import dedent 

#!/usr/bin/env python
import sys
import json
import time
import collections

if sys.version_info >= (3, 0):
    from urllib.parse import urlparse
else:
    from urlparse import urlparse

Otype=''
Osize=0

media_mime = (
'image/',
'video/',
'audio/',
'application/x-shockwave-flash',
'font/',
)

text_mime = (
'application/x-javascript',
'application/javascript',
'application/xml',
'application/json',
'text/',
)


# isodate and dateutil are a bit of an overkill
def mktimeISO8601(s):
    sec, msec = s.split('.', 1)
    
    sec = time.strptime(sec, "%Y-%m-%dT%H:%M:%S")
    sec = time.mktime(sec)
    
    if '+' in msec: msec = msec.split('+', 1)[0]
    elif '-' in msec: msec = msec.split('-', 1)[0]
    msec = msec.replace('Z', '')
    
    return sec + float('0.%s' % msec)


# convert datetimes and urls while parsing json
def jsondecode(el):
    if 'url' in el:
        el['url'] = urlparse(el['url'])
    if 'startedDateTime' in el:
        el['startedDateTime'] = mktimeISO8601(el['startedDateTime'])
    
    return el


def ismedia(entry):
    mtype = entry['response']['content']['mimeType'].split(';')[0]
    for m in media_mime:
        if mtype.startswith(m): return True
    return False

#def localdomain(entry):
#    local=entry['request']['url']
#    #if local
#        #localvar= urlparse(el['url'])
#    return local
    
def istext(entry):
    mtype = entry['response']['content']['mimeType'].split(';')[0]
    for m in text_mime:
        if mtype.startswith(m):
            return True
    return False


def entry_counts(entry, c, k):
    c[k + 'count.total'] += 1
    #c[k + 'requests.local'] += 1
    #c[k + 'requests.external'] += 1
    
    c[k + 'count.media'] += 1 if ismedia(entry) else 0
    c[k + 'count.text']  += 1 if istext(entry) else 0
    
    c[k + 'time.dns'] += entry ['timings']['dns']
    c[k + 'time.transfer'] += entry['timings']['receive'] + \
                              entry['timings']['send']
    
    c[k + 'time.receive']  += entry['timings']['receive']
    c[k + 'time.send']     += entry['timings']['send']
    c[k + 'time.wait']     += entry['timings']['wait']
    c[k + 'time.connect']  += entry['timings']['connect']
    c[k + 'time.blocked']  += entry['timings']['blocked']

 



def entry_Osizes(entry, o, k):
    o[k + 'response.headers'] = entry['response']['headersSize']
    o[k + 'response.bodies'] = entry['response']['bodySize']
    o[k + 'request.headers'] = entry['request']['headersSize']
    o[k + 'request.bodies'] = entry['request']['bodySize']
    o[k + 'content'] += entry['response']['content']['size']

def Otypemedia(entry):
    mtype = entry['response']['content']['mimeType'].split(';')[0]
    for m in media_mime:
        if mtype.startswith(m): 
            return mtype

def Otypetext(entry):
    mtype = entry['response']['content']['mimeType'].split(';')[0]
    for m in text_mime:
        if mtype.startswith(m):
            return mtype

def parsehar(fn):
# @todo: gzip support for python 3.2
    if fn.endswith('.gz'):
        import gzip
        if sys.version_info >= (3, 0):
            import functools
            open_cb = functools.partial(gzip.open, encoding='utf8')
        else:
            open_cb = gzip.open
    else:
        open_cb = open
    
    # parse (possibly gzipped) json 
    with open_cb(fn) as fh:
        # we don't want to deal with negative numbers
        parseint = lambda x: max(int(x), 0)
        data = json.load(fh, object_hook=jsondecode, parse_int=parseint)
        #local=localdomain
    return data


def summarize(data,i):
    counts = c = collections.defaultdict(int)
    objects = o = collections.defaultdict(int)
    #timings = m= collections.defaultdict(int)
    domains = set()
    
    timestamp_min = 2e9  
    timestamp_max = 0
    
    first_entry = None
    urlfirst= data['log']['entries']
    var=0
    for en in urlfirst:
        localone=en['request']['url']
        var=var+1
        if var==1:
            local=localone.netloc

    for entry in data['log']['entries']:
        url = entry['request']['url']
        netloc, path = url.netloc, url.path

    
        # find the earliest request
        started = entry['startedDateTime']
        if isinstance(entry['time'],int):
           finished = started + entry['time']/1000.
        else:
             continue 
        #print type(finished),  type(started) ,  type(entry['time']/1000.)
    
        if finished > timestamp_max:
            timestamp_max = finished
    
        if started < timestamp_min:
            timestamp_min = started
            first_entry = entry
            
        
        if local:
            if netloc == local:
                entry_counts(entry, c, 'requests.local.')
            else:
                entry_counts(entry, c, 'requests.external.')
    
        entry_counts(entry, c, 'requests.')
        
        status = entry['response']['status']
        c['status.redirect'] = 0
        c['status.bad'] = 0
        if 400 > status >= 300:
            c['status.redirect'] += 1
        if status >= 400:
            c['status.bad'] += 1
            
        #entry_Osizes(entry, o, 'Object.')
        #item4=i, [o['Object.response.bodies'],"Resbody", o['Object.response.headers'],"ResHeader"]
        #print item4
        
        if ismedia(entry):
            Otm= Otypemedia(entry)  
            entry_Osizes(entry, o, 'Object.media.')
            if o['Object.media.response.bodies']==-1:
                #print "Object:media",Otm, "Response Body Size",o['Object.media.response.headers'],"Bytes"
                item1=[i, Otm, o['Object.media.response.headers'],"Bytes"]
                #print  i, Otm, o['Object.media.response.headers'],"Bytes"
                #print "writing"
            elif o['Object.media.response.bodies']==0:
                #print "Object:media",Otm, "Response Body Size",0,"Bytes"
                item1=[i, Otm, 0,"Bytes"]
                #print  i, Otm, 0,"Bytes"
                #print "writing"
            else:
                #print "Object:media",Otm, "Response Body Size",o['Object.media.response.bodies'],"Bytes"   
                item1=[i, Otm, o['Object.media.response.bodies'],"Bytes"]
                #print i, Otm, o['Object.media.response.bodies'],"Bytes"
                #print "writing"
        elif istext(entry):
            Ott= Otypetext(entry)  
            #print "Object type:media",Ott
            #print "writing"
            entry_Osizes(entry, o, 'Object.text.')
            if o['Object.text.response.bodies']==-1:
                #print "Object:text",Ott, "Response Body Size",o['Object.text.response.headers'],"Bytes"
                item1=[i, Ott, o['Object.text.response.headers'],"Bytes"]
                #print i,Ott,o['Object.text.response.headers'],"Bytes"
            elif o['Object.text.response.bodies']==0:
                 #print "Object:text",Ott, "Response Body Size",0,"Bytes"
                 item1=[i, Ott, 0,"Bytes"]
                 #print i,Ott, 0,"Bytes"
                 #print "writing"
            else:
                #print "Object:text",Ott, "Response Body Size",o['Object.text.response.bodies'],"Bytes"  
                item1=[i, Ott, o['Object.text.response.bodies'],"Bytes"]
                #print i, Ott, o['Object.text.response.bodies'],"Bytes"
                #print "writing"bodies
            
        # total number of network requests
        domains.add(netloc)
        
    c['requests.domains.count'] = len(domains)
    #c['page.time.onLoad'] = data['log']['pages'][0]['pageTimings']['onLoad']
    c['page.time.onContentLoad'] = data['log']['pages'][0]['pageTimings']['onContentLoad']
    
    #print 'Writing'
    item2=[c['page.time.onContentLoad'], c['requests.count.media'],c['requests.count.text'], c['requests.count.total'], c['requests.domains.count'], c['requests.local.count.text']+c['requests.local.count.media'], c['requests.external.count.text']+c['requests.external.count.media']]
    item5=[c['page.time.onContentLoad']]
    #print item2
    

    #print timings 
    #item3=[i, c['time.dns'] , c['time.transfer'] , c['time.receive'], c['time.send'], c['time.wait'] , c['time.connect'] , c['time.blocked'] ]
    item3=[c['requests.time.dns'] , c['requests.time.transfer'] , c['requests.time.receive'], c['requests.time.send'], c['requests.time.wait'] , c['requests.time.connect'] , c['requests.time.blocked'] ]
    #print item3
    return counts,  objects, item2, item3
    
def serialize(counts, objects,i,  format='plain', prefix='abdn', timestamp=None):
    if timestamp is None:
        timestamp = int(time.time())
        #timestamp = jsondecode
    
    # carbon pickle protocol
    if format == 'pickle':
        from pickle import dumps
        from struct import pack
    
        items = []
        for key, stat in sorted(counts.items()):
            items.append( (key, (timestamp, stat)) )
    
        payload = dumps(items, -1)
        header = pack('!L', len(payload))
        message = header + payload
    
        return message
    
    # carbon line protocol
    if format == 'plain':
        lines = []
        for key, stat in sorted(counts.items()):
            lines.append('%s.%s %s %s' % (prefix, key, stat, timestamp))
            #if key=='requests.time':
            item=[i, key, stat, timestamp]

if __name__ == '__main__':
    from getopt import getopt
    from textwrap import dedent
    o['Object.text.response.bodies']
    usage = '''\
    Usage: python -m harstats_graphite [options] <harfile>
    
    Arguments:
      harfile                  path to HAR file (gzipp    if format == 'plain':
ed or plain)
    
    Options:
      -h, --help               show this help message and exit
      -l, --local <fqdn>       local domain name
      -t, --timestamp <sec>    timestamp to use (default: date +%s)
      -f, --format <arg>       plain or pickle (default: plain)
      -p, --prefix <arg>       metric prefix (default: har.summary)
    
    If the '-l --local' option is given, the script will split request
    statistics into three groups - requests to the local domain, all
    other domains and all requests. Example for 'requests.count':
    
      har.summary.requests.external.count 92 1352934738
      har.summary.requests.local.count 28 1352934738
      har.summary.requests.count 120 1352934738'''
    
    # parse options and arguments
    longopts = ('help', 'local=', 'timestamp=', 'format=', 'path=')
    opts, args = getopt(sys.argv[1:], 'hl:t:f:p:', longopts)
    opts = dict(opts)
    
    if '-h' in opts or '--help' in opts or len(sys.argv) == 1:
        sys.stderr.write(dedent(usage) + '\n')
        sys.exit(1)
    
    timestamp = opts.get('-t') or opts.get('--timestamp') or time.time()
    prefix    = opts.get('-p') or opts.get('--prefix') or 'abdn'
    format    = opts.get('-f') or opts.get('--format') or 'plain'
    local     = opts.get('-l') or opts.get('--local') 
    
    data= parsehar(args[0])
    counts, objects, item2 = summarize(data,i)
    payload = serialize(counts, objects,i, format, prefix, int(timestamp))
    
    fh = sys.stdout
    if sys.version_info >= (3, 0) and isinstance(payload, bytes):
        fh = sys.stdout.buffer
    
    fh.write(payload)
    fh.write('\n')
    
    
    __all__ = 'summarize', 'serialize', 'parsehar'

    

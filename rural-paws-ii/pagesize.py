#script to calculate the page size from a HAR file of web page load
#Written by HassanHamdoun, for Rural Paws project www.dotrural.ac.uk/ruralpaws, University of Aberdeen,  15/03/2015

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

def pgsize(i):
    #sum=0
    #count=0
    #size=0
    bytes=0
    
        
    #f = open('british-business-bank.co.uk+2014-11-04+11-24-05.har', 'r')
    f = open(i, 'r')
    for indx, line in enumerate(f.readlines()):
        pattern = r"headersSize"
        #r=re.compile("startedDateTime*?")
        #var=r.search(line)
        m = re.search(pattern, line)
        if m:   
            x=linecache.getline(i,indx+1)
            x2=''.join(c for c in x if c in digits)
            #print x2
            if int(x2) > 1:
                var=int(x2)
                bytes+=var
                #print 'bytes', bytes
                
                
        pattern2 = r"bodySize"
        #r=re.compile("startedDateTime*?")
        #var=r.search(line)
        n = re.search(pattern2, line)
        if n:
            y=linecache.getline(i,indx+1)
            y2=''.join(c for c in y if c in digits)
            #print x2
            if int(y2) > 1:
                var2=int(y2)
                bytes+=var2
                #print 'bytes', bytes

                    
    pgsizefinal=bytes      
    #print 'Page Size',  pgsizefinal
    return pgsizefinal  
                
#        


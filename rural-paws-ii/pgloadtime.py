#Calculates the page load time from a HAR file for a given web page load process
#Written by HassanHamdoun, for Rural Paws project www.dotrural.ac.uk/ruralpaws, University of Aberdeen,  19/01/2015

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

def ldtime(i):
    index=0
    index1=0
    index2=0
    #sum=0
    #count=0
    #size=0
    loadtime=0
    onload=0
      
    f = open(i, 'r')
    for indx, line in enumerate(f.readlines()):
        pattern = r"startedDateTime"
        #r=re.compile("startedDateTime*?")
        #var=r.search(line)
        m = re.search(pattern, line)
        pattern2=r"onLoad"
        n = re.search(pattern2, line)     
        if m:
            index=indx
            value= line
           #print valueonLoad
            #print index
            if index1==0:
                index1=index
                value1=line
                continue
          
                
        if n:
            indexx=indx
            if index2==0:
                index2=indexx+1
                value2=line
                
    
    y=linecache.getline(i,index1+1)
    timefirst= dparser.parse(y,fuzzy=True)
   # print 'firstime', timefirst
    z=linecache.getline(i,index+1)
    timelast= dparser.parse(z,fuzzy=True)
   # print 'lasttime', timelast
    mm=linecache.getline(i,index2)
    x3=''.join(c for c in mm if c in digits)
    #print x3
    #if x3:
    temp=int(x3)
    onload=int(temp)
    x=linecache.getline(i,index+2)
    if x.find("null")==-1:
        print "fine continue"
        x2=''.join(c for c in x if c in digits)
    #print 'x', x
    #print 'dur', x2
        durlast=int(x2)
        delta=timelast-timefirst
        delta2=int(delta.total_seconds() * 1000) 
        loadtime=delta2+int(durlast)
    else:
        print "null found"
        
    
    return loadtime, onload




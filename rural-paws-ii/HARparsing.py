#python script that gets a HAR files( for a given page load process) and calculates 
#-loadtime
#-onload time 
#-oncontentload time
#- number of media objects
#-number of text objects
#-number of domains
#-number of local requests
#-number of external requests
#-time spent in 
#  a) DNS
#   b) receive
#   d) send 
#   e)wait
#   f)connect
#   g)block
#and saves result to a csv file


#written by hassan hamdoun , hassan@erg.abdn.ac.uk, for rural paws project, 20/01/2014

import objectNumSize as hs
import os 
import csv
from pgloadtime import  ldtime
from pagesize import pgsize
import pickle
import glob
#current=os.getcwd() 
#now=os.chdir("ofsted")
noGovSites=0
loadtimeAll=[]
onloadAll=[]
current=os.getcwd()
now=os.chdir("CaseC")
now2=os.chdir("abdn")
#now3=os.chdir("nowabdn")
with open('abdnCaseC.csv' ,'wb') as fp:
    a=csv.writer(fp, delimiter=',', lineterminator='\n')
    a.writerow(['fID', 'loadtime','onload','pagesize','concontentload','media-count','text-count','total-count', 'count-domains','requests-local','requests-external','DNS', 'transfer','receive','send','wait','connect','blocked'])
    for fn in os.listdir('.'):
#    onload = ")
        if fn.endswith(".har"): 
            print fn
        #print fn
            noGovSites+=1
            f = open(fn, 'r')
            PageSize=pgsize(fn)
            [loadtime, onload]= ldtime(fn)
            loadtimeAll.append(loadtime)
            onloadAll.append(onload)
        #print fn
                
            raw = hs.parsehar(fn)
            data, objects, item2, item3 = hs.summarize(raw, fn)
            print item2

        #print item2
            hs.serialize(data, objects, fn)
            #a.writerow([item2, item3])
            a.writerow([fn, loadtime, onload, PageSize, item2, item3])
            itemf=[fn, loadtime, onload, PageSize, item2, item3]  
            #print 'fID', 'loadtime','onload','pagesize','concontentload','media-count','text-count','total-count', 'count-domains','requests-local','requests-external','DNS', 'transfer','receive','send','wait','connect','blocked'
            print itemf

                
        
        
#fn='139.133.204.23+2015-01-27+15-26-40.har'
#noGovSitesObj+=1
#raw = hs.parsehar(fn)
#data, objects, item2 = hs.summarize(raw, fn)
#        #print item2
#hs.serialize(data, objects, fn)







#original code for overall stats
#import harstatsgraphite as hs
##
#i='139.133.204.23+2014-12-16+16-35-18.json';
#raw = hs.parsehar(i)
#data, started = hs.summarize(raw)
#print(hs.serialize(data, started))



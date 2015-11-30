#script to go through dat acollected propbing a list of urls and return their status 
#- CDN associated with site
#-IP address(A record)
#-PTR record
#-CNAME record 
#-Location record
#-whether domain is cached or not
#assumes a list of text files collecting above info per domain ( from nslookup_Gov_Domains.sh script-see nslookup_Gov_Domains script information)
#NB: need to use Unicode-UTF 8 to read the resulting csv file
#Written by HassanHamdoun, for Rural Paws project www.dotrural.ac.uk/ruralpaws, University of Aberdeen,  15/03/2015

import objectNumSize as hs
import os 
import csv
from pgloadtime import  ldtime
from pagesize import pgsize
import pickle
import glob
import re
import linecache

noGovSites=0
loadtimeAll=[]
onloadAll=[]
current=os.getcwd()
now=os.chdir("CNAMEQFFtemp")
Location=[]
CNAME=[]
A=[]
PTR=[]
Cache=[]
Status=[]
Server=[]

with open('CDNs.csv' ,'wb') as fp:
    a=csv.writer(fp, delimiter=',', lineterminator='\n')
    a.writerow(['site' ,'Location','CNAME','A', 'PTR', 'Server', 'Status', 'Cache'])
    for fn in os.listdir('.'):
        if fn.endswith(".txt"): 
            noGovSites+=1
            print fn
            f = open(fn, 'r')
            for indx, line in enumerate(f.readlines()):
                if indx==0:
                    site=line.split(None, 1)[0]
                    
                pattern2 = r"Location"
                m2=re.search(pattern2, line)
                if m2:
                    indexx=indx
                    Location=linecache.getline(fn,indexx+1)
                    Location=Location.split(None, 1)[1]

                pattern6 = r"Server"
                m6=re.search(pattern6, line)
                if m6:
                    index6=indx
                    Server=linecache.getline(fn,index6+1)
                    Server=Server.split(None, 1)[1]
                            #print fn

                pattern7 = r"X-Cache"
                m7=re.search(pattern7, line)
                if m7:
                    index7=indx
                    Cache=linecache.getline(fn,index7+1)
                    Cache=Cache.split(None, 1)[1]
                    
                pattern8 = r"Status"
                m8=re.search(pattern8, line)
                if m8:
                    index8=indx
                    Status=linecache.getline(fn,index8+1)
                    Status=Status.split(None, 1)[1]
                
                pattern10 = r"CNAME"
                m10=re.search(pattern10, line)
                if m10:
                    index10=indx
                    CNAME=linecache.getline(fn,index10+2)

                   #CNAME=CNAME.split(' ')
                pattern4 = r"IP"
                m4=re.search(pattern4, line)                    
                if m4:
                    index4=indx
                    A=linecache.getline(fn,index4+1)
                    A=A.split(' ')
                    
                pattern5 = r"PTR"
                m5=re.search(pattern5, line)
                if m5:
                    index5=indx
                    PTR=linecache.getline(fn,index5+2)
                    PTR=PTR.split(' ')
                    


            a.writerow([site, Location, CNAME, A,  PTR, Server, Status, Cache])
            itemf=[site, Location, CNAME, A, PTR, Server, Status, Cache]  
            print itemf

            
        
        

# -*- coding: utf-8 -*-

'''import someting tools'''
from base import *
import re
import hashlib
import xml.dom.minidom


class chrome(importer):
    ''' import google chrome bookmark file to a tree'''
    def __init__(self):
        importer.__init__(self)
        self.token=[]#token
        self.folders=[]#FILO Stack of parent folders
        self.md5 = hashlib.md5()
        
    #==pasrer start 
    def importfromfile(self,filename):
        '''import file to a tree'''
        with open(filename,"r") as file:
            data = file.read()
            self.lines=data.split("\n")#TODO: if not has \n
            self.tree.create_node(0,0,data=bkdata({"url":"ll"}))# the root 
            self.totree(self.lines)
            
    def totree(self,lines):
        
        #pasrer
        for l in lines :
            m=re.search(r'.*DL>.*',l)#about folder 
            if m :
                if re.search(r'.*/DL>.*',l): #end folder 
                    self.token.append(1)
                else :
                    if re.search(r'.*<H3.*',l):
                        self.token.append(2) #folder title 
                    else :
                        self.token.append(3) # into a folder 
            else:
                self.token.append(4) #other
        for k in map(lambda i,s,l:(i,s,l), range(len(lines)),self.token, lines):
            if k[1]==3:
                self.isfolder(k[0],k[2])
            elif k[1]==1:
                self.outfolder()
            elif k[1]==4:
                if re.search(r'.*<A.*',k[2]):# a bookmark 
                    self.ismark(k[0],k[2])
                    
    def ismark(self,index,line):

        #very stupid
        x=line.replace("<DT>","<xml>").replace("</A>","</A></xml>").replace("&","&amp;")
        dom = xml.dom.minidom.parseString(x)
        A = dom.getElementsByTagName("A")[0]
        
        #some data
        data={
        "title":A.firstChild.data or "",
        "url":A.getAttribute("HREF") , #must !!!
        "add_date":A.getAttribute("ADD_DATE") or 0,
        "last_visit":A.getAttribute("LAST_VISIT") or 0,
        "last_modified":A.getAttribute("LAST_MODIFIED") or 0,
        # what this ?
        "lovefav":A.getAttribute("LOVEFAV") or 0,
        "fav_pos":A.getAttribute("FAV_POS"),
        #end
        }
        
        #get the hash 
        self.md5.update(self.geturlbody(data["url"]).encode("gbk"))
        index=self.md5.hexdigest() 
        data["index"]=index
        self.tree.create_node(index,index,parent=self.folders[len(self.folders)-1],data=bkdata(data))
    
    def isfolder(self,index,line):
        #HERE!!!
        i=index-1
        if len(self.folders)==0:
            self.tree.create_node(i,i,parent=0,data=bkdata({"url":""}))
        else:
            self.tree.create_node(i,i,parent=self.folders[len(self.folders)-1],data=bkdata({"url":""}))
        self.folders.append(i)
        
    def outfolder(self):
        self.folders.pop()
    #===== pasrer end
        

if __name__=="__main__":
    test=chrome()
    test.importfromfile("chrome_test.html")
    test.showtree()
    
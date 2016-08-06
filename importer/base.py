# -*- coding: utf-8 -*-

from treelib import *
import urlparse

class bkdata(object):
    
    def __init__(self,data):
        for k in data :
            setattr(self,k,data[k])

class importer(object):
    '''importer'''
    def __init__(self):
        self.tree=Tree()
        pass
    def gettree(self):
        return self.tree()
    def showtree(self, data_property= None):
        self.tree.show( data_property= data_property)
    def ismark(self,**arg):
        pass
    def isfolder(self,**arg):
        pass
    def geturlbody(self,url):
        ''' http://www.baidu.com/       -->www.baidu.com/
            https://ww.baidu.com/       -->www.baidu.com/
        '''
        r=urlparse.urlparse(url)
        return  r.netloc+r.path+(r.query and "?"+r.query or "")
    def allbookmark(self):
        for k in self.tree.expand_tree():
            if not self.tree.children(k):
                 yield self.tree.get_node(k)
    def allfolder(self):
        for k in self.tree.expand_tree():
            if  self.tree.children(k):
                 yield self.tree.get_node(k)
    def apply(self,fn):
        pass

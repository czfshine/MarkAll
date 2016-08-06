# -*- coding: utf-8 -*-
''' The bookmark data '''
import sqlite3

class bkbase(object):
    
    def __init__(self,filename):
        self.conn=sqlite3.connect(filename,timeout=1)
        self._initbase_()
        self.bkid=0
        self.folderid=0
        
    def _initbase_(self):
        self.conn.execute('''CREATE TABLE  IF NOT EXISTS bookmarks
        (id INT PRIMARY KEY     NOT NULL,
         url            TEXT    NOT NULL,
         parentfolder   INT     NOT NULL,
         title          TEXT     ,
         ico            TEXT,
         comment        TEXT
       );''')
       
        self.conn.execute('''CREATE TABLE   IF NOT EXISTS folders
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       parent         INT     NOT NULL,
       comment        TEXT);''')
        self.conn.commit()
        pass
    def addbookmark(self,url,parentid,title="NULL",icodata="NULL",commenttext="NULL"):
        
        res=self.conn.execute("select max(id) from bookmarks").fetchall()[0][0]
        if res:
            self.bkid=res+1
            
        self.conn.execute("INSERT INTO bookmarks (id,url,parentfolder,title,ico,comment) \
      VALUES (%d, %s, %d, %s, %s,%s )"%(self.bkid,url,parentid,title,icodata,commenttext))
        pass
    
    def addfolder(self):
        
        res=self.conn.execute("select max(id) from folders").fetchall()[0][0]
        if res:
            self.foldersid=res+1
            
        self.conn.execute("INSERT INTO folders (id,name,parent,comment) \
      VALUES (%d, %s,%d,%s )"%(self.folderid,"",1,""))
        pass
    
    def close(self):
        self.conn.commit()
        self.conn.close()
        pass
    
b=bkbase("test.db")
b.addbookmark(2,2,2)
b.addfolder()
b.close()

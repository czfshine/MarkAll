# -*- coding: utf-8 -*-

''' export to baidu kity minder json 

The kityminder website :
    https://github.com/fex-team/kityminder
    
from kityminder to json:
    In brower console type: editor.minder.exportData("json").fulfillValue
from json to kityminder:
    type: editor.minder.importData("json","The json string")

a kity data example:
define：
    root    :=note,template,theme,version
    note    :=data,children
    children:=(note[,note]*)
    data    :=id[str],title[str],created[int][,other*]
    other   :=priority|progress|resource|....

{"root":

    {"data":
        {"id":"b67sp8d6aego",
        "created":1470567581026,
        "text":"中心主题"},
        
     "children":[
     
         {"data":
             {"id":"b67sxvu2fhcg",
             "created":1470568258995,
             "text":"分支主题",
             "priority":1,
             "progress":1,
             "resource":["WTF","one"],
             "note":"BTW: This a note:)",
             "image":"http://127.0.0.1:7283/dist/images/iconpriority.png",
             "imageTitle":"114",
             "imageSize":{"width":20,"height":200},
             "hyperlink":"http://127.0.0.1:7283/dist/images/iconpriority.png",
             "hyperlinkTitle":"http://127.0.0.1:7283/dist/images/iconpriority.png",
             "font-family":"arial black,avant garde",
             "font-size":24,
             "font-style":"italic",
             "font-weight":"bold",
             "color":"#4f81bd",
             "background":"#9bbb59"},
        "children":[]
        }
        
        ]
    },
    "template":"default",
    "theme":"fresh-blue",
    "version":"1.4.33"}
'''
import json
import re
import hashlib
class kity(object):
    
    def __init__(self):
        self.dict={}
        self.json={}
        self. md5 = hashlib.md5()
        self.rules='''
        bookmark data to kityminder data[type]
        add_date-->created[int]
        url-->hyperlink[str]
        title-->hyperlinkTitle[str]
        title-->text[str]
        '''
        
    def getjson(self):
        self.dict["template"]="default"
        self.dict["theme"]="fresh-blue"
        self.dict["version"]="1.4.33"
        return json.dumps(self.dict)
    
    def importfromtree(self,tree,nid):
        self.tree=tree
        self.dict=self.to_dict()
        
    def format(self,child):
        for k in child :
            return child[k]
          
            
    def to_dict(self, nid1=None):
        
        tree=self.tree
        
        nid = tree.root if (nid1 is None) else nid1
        ntag ="root"  if (nid1 is None) else tree[nid].tag
        tree_dict = {ntag: {"children": []}}

        t={"id":self.getid("czfshine")}
        tree_dict[ntag]["data"] = self.replace(tree[nid].data.to_dict(),t)
        
        if tree[nid].expanded:
            queue = [tree[i] for i in tree[nid].fpointer]
            for elem in queue:
                tree_dict[ntag]["children"].append(self.format(self.to_dict(elem.identifier)))
            if len(tree_dict[ntag]["children"]) == 0:
                tree_dict = tree[nid].tag if not True else \
                            {ntag: {"data":self.replace(tree[nid].data.to_dict(),t)}}
        return tree_dict
    def replace(self,dict,target):
        
        for r in self.rules.split("\n") :
            m=re.search(r'(.*)\-\-\>(.*)\[(.*)\]',r)
            if m:
                t=m.groups()
                
                _from=t[0].replace(" ","")
                _to=t[1]
                _type=t[2]
                
                target[_to]=dict.get(_from,"")
        return target
    def getid(self,something):
        self.md5.update(something)
        return self.md5.hexdigest()[0:12]
# -*- coding: utf-8 -*-

''' export to baidu kity minder json 

The kityminder website :
    https://github.com/fex-team/kityminder
    
from kityminder to json:
    In brower console type: editor.minder.exportData("json").fulfillValue
from json to kityminder:
    type: editor.minder.importData("json","The json string")

a kity data example:

"{"root":

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
    "version":"1.4.33"}"

define：
    root    :=note,template,theme,version
    note    :=data,children
    children:=(note[,note]*)
    data    :=id[str],title[str],created[int][,other*]
    other   :=priority|progress|resource|....
'''
class kity(object):
    
    def __init__(self):
        pass
    
    def importfromtree(self,tree,nid):
        self.tree=tree
        
        print self.tree.to_dict(with_data=True)
        pass
    
    def tojson(self):
        pass
    

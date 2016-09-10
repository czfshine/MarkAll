# MarkAll
A tool for browser bookmarks.

### Features
* It can import base on chromium browser's bookmark file .
* It can export to the KityMinder.

### usage

#### from chrome to kity minder :
* clone this repoository into you PC
* install requirable library `pip install treelib `
* run follow code
```python 

# import something
import importer.chrome as chrome 
import exporter.kity as kity

# import from chrome bookmark file 
c=chrome.chrome()
c.importfromfile("./importer/chrome_test.html")
#c.showtree("title")

# the bookmark tree
t=c.gettree()

#export to kityminder json
k=kity.kity()

k.importfromtree(t,None)
print "editor.minder.importData(\"json\",'"+k.getjson()+"')"
#copy the output to the brower console
```


### support

my e-mail : czfshine#outlook.com
QQ :1486276329

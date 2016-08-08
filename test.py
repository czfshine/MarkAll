# -*- coding: utf-8 -*-

import importer.chrome as chrome 


test=chrome.chrome()

test.importfromfile("./importer/chrome_test.html")

test.showtree("title")

t=test.gettree()

print t

import exporter.kity as kity

k=kity.kity()

k.importfromtree(t,None)
print "editor.minder.importData(\"json\",'"+k.getjson()+"')"

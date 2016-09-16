# -*- coding: utf-8 -*-

import importer.chrome as chrome 
import exporter.kity as kity
import cProfile
import pstats

def testt():
    test=chrome.chrome()
    test.importfromfile("./temp/bookmarks_16_8_11.html")
    #test.showtree("title")
    t=test.gettree()
    k=kity.kity()
    k.importfromtree(t,None)
    t=k.getjson()
    #print "editor.minder.importData(\"json\",'"+k.getjson()+"')"
    
cProfile.run("testt()", "profilerdata")
p = pstats.Stats("profilerdata")
p.strip_dirs().sort_stats(-1).print_stats()
p.strip_dirs().sort_stats("tottime").print_stats()
p.strip_dirs().sort_stats("cumulative").print_stats(3)
p.print_callers(0.5, "testt")
p.print_callees("testt")

#testt()
### use this in a hive transformation
###
### assume this table exits
###
### create table cnn_top (title string, link string, source string) ;
###
### to cmd line test this:
###   echo "{ \"title\" : \"james muguira\", \"link\" : \"http://rss.cnn.com/rss/cnn_topstories.rss\", \"source\" : \"hello world\", \"data\" : \"{ json }\" }"
###
### for example
###
###   insert into table cnn_top select transform (text) 
###     using 'python map_strm.py' as (title, link, source, data) 
###     from test;

###

import sys
import json
from   pattern.vector import Document
from   pattern.web import plaintext
import urllib2


for line in sys.stdin:
	line = line.strip()
	ljs = json.loads(line)
	fjs = urllib2.urlopen(ljs['link']).read()
	st = plaintext(fjs)
	d = Document(st)
	w = json.dumps(d.keywords())
	print "%s\t%s\t%s\t%s" % (ljs['title'], ljs['link'], ljs['source'], w)
	



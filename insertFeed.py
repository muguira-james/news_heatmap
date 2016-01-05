###
### transform the input rss url into a "title, link, source" tupple
###
### output is the file: test.json, 
###
import sys
import feedparser
import urllib2
import json

### a class to tidy up the processing
class Article(object):
    def __init__(self, source, title, link):
        self.source = source
        self.title = title
        self.link = link

### this will dump the class variables as a dictionary
def jdefault(o):
    return o.__dict__

### ----------------------- code -------------------

if ( len(sys.argv) < 2):
    print "usage: insertFeed url"
    sys.exit(1)

url = sys.argv[1]
file = open("test.json", "w")

### an example urL
### url = 'http://rss.cnn.com/rss/cnn_topstories.rss'

d = feedparser.parse(url)
cnt = 0
for post in d.entries:
    ar = Article(url, post.title, post.link)
    ### dump it to json
    ar_json = json.loads(json.dumps(ar, default=jdefault))
    file.write(json.dumps(ar, default=jdefault))
    file.write('\n')
    cnt = cnt + 1

print cnt




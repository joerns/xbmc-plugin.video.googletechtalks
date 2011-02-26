import urllib2
import xml.dom.minidom

class YouTubeVideo:
    def __init__(self):
        self.title = None
        self.id = None
        self.published = ""
        self.updated = ""
        self.description = "descr"

    def __str__(self):
        if self.title == None:
                return "<None>"
        else:
            return "[%s][%s] %s" %(self.id, self.published, self.title)

def data(page = 1, max_results = 10):
    url = "http://gdata.youtube.com/feeds/api/videos?"\
        "max-results=%d&start-index=%d&author=GoogleTechTalks&orderby=published"\
        % (max_results, (page-1)*max_results+1)

    return urllib2.urlopen(url).read()

def parse_text_node(node, tag):
    s = ""

    for tagnode in node.getElementsByTagName(tag):
        for n in tagnode.childNodes:
            if n.nodeType == n.TEXT_NODE:
                s = s + (n.data.strip())

    return s

            
def parse_document(node):
    x = []
    
    for n in node.getElementsByTagName("entry"):
        elem = YouTubeVideo()
  
        elem.title = parse_text_node(n, "title")
        elem.id = parse_text_node(n, "id").split("/")[-1]
#        elem.id = parse_text_node(n, "yt:videoid")
        elem.published = parse_text_node(n, "published")
        elem.updated = parse_text_node(n, "updated")
        elem.description = parse_text_node(n, "media:description")
        x.append(elem)

    return x



dom = xml.dom.minidom.parseString(data(1,25))
elems = parse_document(dom)
i = 1
for e in elems:
    print i, str(e)
    i += 1


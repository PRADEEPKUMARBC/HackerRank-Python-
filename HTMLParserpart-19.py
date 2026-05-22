# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            if(attr[1]==None):
                print("-> "+ attr[0] +" > " + str(None))
            else:
                print("-> "+ attr[0] +" > " + attr[1])
    def handle_endtag(self,tag):
        print("End   :", tag)
    def handle_startendtag(self,tag,attrs):
        print("Empty :", tag)
        for attr in attrs:
            if(attr[1]==None):
                print("-> "+ attr[0] +" > "+str(None))
            else:
                print("-> "+ attr[0]+" > "+attr[1])
                
parser = HTMLParser()
N = int(input())
for _ in range(N):
    parser.feed(input())

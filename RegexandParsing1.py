# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class myhtmlparser(HTMLParser)
    def handle_starttag(self,tag,attrs)
        if not attrs
            print(tag)
        if attrs
            print(tag)
            for attr in attrs
                print(-,attr[0],,attr[1])
html = 
for _ in range(int(input()))
    html += input()
parser = myhtmlparser()
parser.feed(html)
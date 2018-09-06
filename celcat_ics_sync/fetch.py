import urllib.request as urlreq
import re


def getjseventlist(url):
    try:
        html = urlreq.urlopen(url).read().decode("utf-8")

        res=re.findall(r'<script\s*[^>]*\s*>(.*?)</script', html, re.I|re.S)
        for match in res:
            for line in match.split('\n'):
                eventjslist = re.findall(r'v\.events\.list\s=\s(\[.*\]);',line,  re.I|re.S)
                if(len(eventjslist) == 1): # matched
                    print("yay")
                    return eventjslist[0];
    except URLError:
        print("URL Error")

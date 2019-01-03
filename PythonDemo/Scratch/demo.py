import urllib.request
 
respone = urllib.request.urlopen("http://www.baidu.com")
html = respone.read()
print(html)
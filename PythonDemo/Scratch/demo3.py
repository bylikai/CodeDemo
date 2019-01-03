import  ssl
import  urllib
import  urllib.request
import  urllib.parse
import  urllib.error
import  http.cookiejar
import  re      #import regular expressions
#from bs4 import BeautifulSoup

#准备数据：url,请求数据data,ssl访问方式,请求头headers
url = "https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://matcloud.cnic.cn/api/account/user/escience_cn_callback&client_id=78349&theme=simple"
data = urllib.parse.urlencode( {'userName':'bylikai@163.com', 'password':'luoye008'} ).encode("utf-8")
context = ssl._create_unverified_context()

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
         'Referer':'http://matcloud.cnic.cn/static/view/signin.html'}

#设置代理请求 ,（设置调试日志级别 debuglevel）
proxy_handler = urllib.request.ProxyHandler({'http':'http://some-proxy.com:8080'})
http_handler  = urllib.request.HTTPHandler(debuglevel=0)
https_hander  = urllib.request.HTTPSHandler(debuglevel=0)
#opener = urllib.request.build_opener( proxy_handler )
#opener = urllib.request.build_opener( proxy_handler,http_handler, https_hander )
#urllib.request.install_opener( opener )

#使用cookie
cookie = http.cookiejar.CookieJar()
httpCookieProcessor = urllib.request.HTTPCookieProcessor( cookiejar=cookie )
opener = urllib.request.build_opener( httpCookieProcessor )
urllib.request.install_opener( opener )

#发出请求以及响应对象 : urlopen最终调用返回  return opener.open(url, data, timeout)
localRequest  = urllib.request.Request(url, data, headers )

#添加异常处理： try/except  ( ErrorType as err)
try:
    localResponse = urllib.request.urlopen( localRequest,  timeout=10, context=context)

#获取响应数据
    html =  localResponse.read().decode('utf-8')
    print(html)

#获取cookie
    for item in cookie:
        print("Name is %s , Password is %s \n" %(item.userName, item.password) )    
except urllib.error.HTTPError as err:
    print(err)
except urllib.error.URLError as err:
    print(err)
except :
    print("exception")

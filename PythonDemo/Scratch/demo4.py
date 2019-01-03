import  ssl
import  urllib
import  urllib.request
import  urllib.parse
import  urllib.error
import  http.cookiejar
import  re      #import regular expressions
from bs4 import BeautifulSoup
import lxml

#准备数据：url,请求数据data,ssl访问方式,请求头headers
url = "https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://matcloud.cnic.cn/api/account/user/escience_cn_callback&client_id=78349&theme=simple"
data = urllib.parse.urlencode( {'userName':'bylikai@163.com', 'password':'luoye008'} ).encode("utf-8")
context = ssl._create_unverified_context()

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
         'Referer':'http://matcloud.cnic.cn/static/view/signin.html'}


#发出请求以及响应对象 : urlopen最终调用返回  return opener.open(url, data, timeout)
localRequest  = urllib.request.Request(url, data, headers )

#添加异常处理： try/except  ( ErrorType as err)
try:
    localResponse = urllib.request.urlopen( localRequest,  timeout=10, context=context)

#获取响应数据
    html =  localResponse.read().decode('utf-8')
    print(html)

#正则表达式解析内容
    pattern = re.compile( r"userName" )

    ## match 0位置匹配
    result1 = re.match( pattern, html )
    if result1:
        print( result1.group() )
    else :
        print("match error!")

    ## search 任意位置匹配
    result2 = re.search( pattern, html )
    if result2:
        print(result2.group())
    else:
        print("search error!")

    ## BeautifulSoup
    #html_doc = html[ html.find("<html>") :  html.rfind("</html>") ] + "</html>"
    html_doc = '''
     <html>
        <head>
        <title>
            The Dormouse's story
        </title>
        </head>
        <body>
        <p class="title">
            <b>
            The Dormouse's story
            </b>
        </p>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a class="sister" href="http://example.com/elsie" id="link1">
            Elsie
            </a>
            ,
            <a class="sister" href="http://example.com/lacie" id="link2">
            Lacie
            </a>
            and
            <a class="sister" href="http://example.com/tillie" id="link2">
            Tillie
            </a>
            ; and they lived at the bottom of a well.
        </p>
        <p class="story">
            ...
        </p>
        <p>
            Please input password : <input type="password" name="password" />
        </p>
        </body>
        </html>
    '''

# 选择不同的解析方式来解析html:  python自带解析html.parser, lxml, html5lib 
# 建议使用 lxml 速度快，功能强大
    #soup = BeautifulSoup(html_doc, 'html.parser' )
    soup = BeautifulSoup(html_doc, 'lxml' )
    print( soup.prettify() )
    print( soup.get_text() )
    print( soup.title )
    print( soup.title.name )
    print( soup.title.string )
    print( soup.head )

    for link in soup.find_all('a') :
        print( link.get('href') )

except urllib.error.HTTPError as err:
    print(err)
except urllib.error.URLError as err:
    print(err)

print("@Finish!@")
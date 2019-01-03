import  ssl
import  urllib
import  urllib.request
import  urllib.parse
import  urllib.error
import  http.cookiejar
import  re      #import regular expressions
from bs4 import BeautifulSoup
import lxml

'''
    详细解析每一个项目详细信息
'''

#准备数据：url,请求数据data,ssl访问方式,请求头headers
url = "http://bid.powerchina.cn/announcement/getAnnouncementDetails.html?id=180527900"


#发出请求以及响应对象 : urlopen最终调用返回  return opener.open(url, data, timeout)
localRequest  = urllib.request.Request(url )

try:
    localResponse = urllib.request.urlopen( localRequest,  timeout=10 )

#获取响应数据
    html =  localResponse.read().decode('utf-8')
    #print( html )

#正则表达式解析内容
# 选择不同的解析方式来解析html:  python自带解析html.parser, lxml, html5lib 
# 建议使用 lxml 速度快，功能强大
    #soup = BeautifulSoup(html_doc, 'html.parser' )
    soup = BeautifulSoup(html, 'lxml' )
    #print( soup.prettify() )
    print( soup.get_text() )

# 解析内容

except urllib.error.HTTPError as err:
    print(err)
except urllib.error.URLError as err:
    print(err)

print("@Finish!@")
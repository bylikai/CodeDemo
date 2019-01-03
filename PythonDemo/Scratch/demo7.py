import  ssl
import  urllib
import  urllib.request
import  urllib.parse
import  urllib.error
import  http.cookiejar
import  re      #import regular expressions
from bs4 import BeautifulSoup
import lxml

import csv
import codecs

'''
    获取项目列表信息
'''

#准备数据：url,请求数据data,ssl访问方式,请求头headers
url = "http://bid.powerchina.cn/announcement/getGengDuo"
##  type
##  0:-类-型-
##  7:工程类
##	9:服务类
##  8:设备物资

def get_project_list( page ) :
    '''
    get the project the list
    '''
    data = urllib.parse.urlencode( {'typeed':4, "type":0, 'page':page, "title":"", "menu":"", "start":"2018-01-01", "end":"" } ).encode("utf-8")
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}


    #发出请求以及响应对象 : urlopen最终调用返回  return opener.open(url, data, timeout)
    localRequest  = urllib.request.Request(url, data, headers )

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
        
    # 获取列表
        count = 0
        for link in soup.find_all(href=re.compile("id=")) :
            title = link.text.strip()
            href =  "http://bid.powerchina.cn" + link.get('href')
            title_u = title

            writer.writerow([title_u,href])
            count += 1        
        return count
    except urllib.error.HTTPError as err:
        print(err)
    except urllib.error.URLError as err:
        print(err)
    return 0

# 从列表写入csv文件
csvFile = open('powerchina.csv','a', encoding='utf-8', newline='')
writer = csv.writer( csvFile )

page = 1
while True:
    if( 0==get_project_list(page) ) :
        break
    page += 1

csvFile.close()

print("@Finish!@")
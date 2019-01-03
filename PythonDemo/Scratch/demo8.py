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
class ProjectItem:
    def __init__(self, title, href ):
        self.title = title
        self.href   = href
    

class ProjectList:
    
    def __init__(self, base, url):
        self.base = base
        self.url  = url
        self.headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    
    def request_data_list(self, data):

        # 发出请求
        localRequest  = urllib.request.Request(self.url, data, self.headers )        
        try:
            localResponse = urllib.request.urlopen( localRequest,  timeout=10 )
            
            #获取响应数据
            html =  localResponse.read().decode('utf-8')
            soup = BeautifulSoup(html, 'lxml' )
        
            # 获取列表
            result_list = []
            for link in soup.find_all(href=re.compile("id=")) :                
                title = link.text.strip()
                href =  link.get('href')
                if href.index('/') == 0 :
                    href = self.base + href
                item = ProjectItem( title, href )

                result_list.append( )
        except urllib.error.HTTPError as err:
            print(err)
        except urllib.error.URLError as err:
            print(err)
    


print("@Finish!@")
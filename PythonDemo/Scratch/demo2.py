import  ssl
import  urllib
import  urllib.request
import  urllib.parse

#准备数据：url,请求数据data,ssl访问方式
url = "https://passport.escience.cn/oauth2/authorize?response_type=code&redirect_uri=http://matcloud.cnic.cn/api/account/user/escience_cn_callback&client_id=78349&theme=simple"
data = urllib.parse.urlencode( {'userName':'bylikai@163.com', 'password':'luoye008'} ).encode("utf-8")
context = ssl._create_unverified_context()

#发出请求以及响应对象
localRequest  = urllib.request.Request(url, data)
localResponse = urllib.request.urlopen( localRequest,  context=context)

#获取响应数据
html =  localResponse.read().decode()
print(html)
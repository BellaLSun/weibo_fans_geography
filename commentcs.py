import requests
import re  # regex
import time # sleep（） 防止被封IP

# 不要放多进程，会被封IP。小网站的话会拖垮别人的网址

# 动态加载
url ='https://m.weibo.cn/api/comments/show?id=4272646034265355&page=1'
# 请求网址，得到json文件信息
html = requests.get(url) # 获得网页源代码
print(html)
# print(html.json())

# json， so no need to regex， （dictionary）with slice is much easier
# json and dictionary 高度兼容

data = html.json()['data']['data'][0]['text']
print (data)


### 正式开始
ii = 0 # 数值型，所以后边要改一下
while ii <=10:  # 页数
    ii = ii + 1
    url ='https://m.weibo.cn/api/comments/show?id=4272646034265355&page='+str(ii)
    time.sleep(3)
    html = requests.get(url)
    try:
        for jj in range(len(html.json()['data']['data'])):
            data = html.json()['data']['data'][jj]['text']
            # 写入本地
            # with open（）不用主动关闭文件
            with open('鹿晗.txt','a') as ff:
                # 汉字不能再用json文件了，要用正则了
                # \u4e00-\u9fa5 汉字编码
                # 提取data变量中的所有汉字信息
                # findall 返回的是列表格式
                # comments = re.findall('[\u4e00-\u9fa5]',data)
                # print (comments)   # 会把评论都拆成一个字一个字的。
                # 要再把这个拼接起来

                # data = html.json()['data']['data'][0]['text']
                comments = ''.join(re.findall('[\u4e00-\u9fa5]', data))
                # 写入文件
                ff.write(comments + '\n')
    except:
        None


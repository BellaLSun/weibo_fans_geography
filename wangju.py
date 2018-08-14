import requests
import re  # regex
import time # sleep（） 防止被封IP
import json


# wangju id:  4272656989213465

comment_parameter = []  # 用来存放微博url参数
comment_url = []  # 用来存放微博url
user_id = []  # list：用来存放user_id
comment = []  # 用来存放评论
containerid = []  # 用来存放containerid
feature = []  # 用来存放用户信息

# get user_id

ii = 0 # 数值型，所以后边要改一下
while ii <=5:  # 页数
    ii = ii + 1
    url ='https://m.weibo.cn/api/comments/show?id=4272656989213465&page='+str(ii)
    time.sleep(1)
    html = requests.get(url)
    for i in range(len(html.json()['data']['data'])):
        # 必须新命名一个变量，不然就不是user_id就不再是列表了,就不能再用append方法了
        # https://fishc.com.cn/thread-97640-1-1.html
        one_user_id = html.json()['data']['data'][i]['user']['id']
        user_id.append(one_user_id)
print( user_id)


# get container ID
# https://m.weibo.cn/api/container/getIndex?type=uid&value=5170266361
user_base_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value="
id = []
for id in list(user_id,):  #需要对user_id去重
    containerid_url = user_base_url + str(id)
    try:
        con_r = requests.get(containerid_url)
        one_containerid = con_r.json()['data']['tabsInfo']['tabs'][0]['containerid']
        containerid.append(one_containerid)
    except:
        containerid.append(0)
print(containerid)

# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组）
# 然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压）
for i,j in zip(user_id, containerid,):
    url = "https://m.weibo.cn/api/container/getIndex?uid=" + str(
       i) + "&luicode=10000011&lfid=100103type%3D1%26q%3D&featurecode=20000320&type=uid&value=" + str(
        i) + "&containerid=" + str(j)
    html = requests.get(url)
    try:
        data = html.json()["data"]["cards"][0]["card_group"][0]["item_content"].split("  ")
        with open('王菊fans.txt','a') as ff:
            ff.write(data[0] + '\n')
            time.sleep(1)
    except:
        None

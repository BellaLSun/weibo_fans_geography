# coding:utf-8
from pyecharts import Style
from pyecharts import Geo
import json
import io
import codecs

filename = 'province_coordinates.json'
def keshihua(filepath):
    city = []
    with io.open(filepath, mode='r', encoding='utf-8') as f:
        rows = f.readlines()

        for row in rows:
             try:
                city.append(row.split(' ')[1].replace('\n', ''))
             except:
                city.append('none')
    def all_list(arr):
        result = {}
        for i in set(arr):
            result[i] = arr.count(i)
        return result

    data = []
    for item in all_list(city):
        data.append((item, all_list(city)[item]))
        style = Style(
            title_color="#fff",
            title_pos="center",
            width=1200,
            height=600,
            background_color="#404a59"
        )

    geo = Geo("王菊粉丝人群地理位置", "ZGM", **style.init_style)
    attr, value = geo.cast(data)
    print("data:", json.dumps(data, ensure_ascii=False))
    print("attr:", json.dumps(attr, ensure_ascii=False))
    print("value:", value)

    geo.add_coordinate(u"荷兰",0,0)
    geo.add_coordinate(u"马来西亚", 0, 0)
    geo.add_coordinate(u"越南", 0, 0)
    geo.add_coordinate(u"印度", 0, 0)
    geo.add_coordinate(u"希腊", 0, 0)
    geo.add_coordinate(u"昌都", 0, 0)
    geo.add_coordinate(u"none", 0, 0)
    geo.add_coordinate(u"新加坡", 0, 0)
    geo.add_coordinate(u"加拿大", 0, 0)
    geo.add_coordinate(u"澳大利亚", 0, 0)
    geo.add_coordinate(u"其他", 0, 0)
    geo.add_coordinate(u"美国", 0, 0)
    
    geo.add("", attr, value, visual_range=[0, 120],
            visual_text_color="#fff", symbol_size=20,
            is_visualmap=True, is_piecewise=True,
            visual_split_number=4)

    geo.render("fans_geo.html")

filepath ='王菊fans.txt'
keshihua(filepath)

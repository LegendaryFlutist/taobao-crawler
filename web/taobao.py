# -*- coding: utf-8 -*-
import requests
import re
import time
import urllib
import os

# 此处写入登录之后自己的cookies
cookie = 'thw=cn; enc=OLCmDlTxIBBE4a6RiWh8ul8sB6YTZtjT8hTTU5v5UFq43VKJZlr7XKqgNrmaLFDMyrWWbyrW0V3plmztcwbnHA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; cna=lFOpFrKbYmgCAd5aUqjS59Lp; sgcookie=EvhX7M0onuQW2YEa6GTZp; uc3=nk2=rTHgfmQo%2B3URT7M%3D&vt3=F8dBxGDWM9bjcSvyyQQ%3D&id2=UoTV7NMSt7LwuQ%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; lgc=%5Cu552F%5Cu5FC3%5Cu4E0D%5Cu6613166; uc4=id4=0%40UOx%2FVCdtTk3F4hnTqZzynBsD3loK&nk4=0%40r8DeBACISRw4OBU0OOpxxxgEovJ2YA%3D%3D; tracknick=%5Cu552F%5Cu5FC3%5Cu4E0D%5Cu6613166; _cc_=Vq8l%2BKCLiw%3D%3D; mt=ci=2_1; tfstk=cW9hButuJB5BtIGNHv6Bq-4RMoMAa-ePoLJ6QpNw_jE5YPpNqsHLNDisfg3DUL5..; lLtC1_=1; miid=627810441533658654; t=57f13cda9df51fbf6c629b585437d59c; cookie2=1f2a2308e551b7d6627445a500b045ac; v=0; _tb_token_=5f3383ef768b3; _samesite_flag_=true; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hoq1WlskoPDxV487noKFxVxlm0Rlly9CyZtqLvHiJzSdoqp5BgqzPYtcI0dNRkLVMmHWX6kP%2Bl%2Fiwr7VRpyBuxgzNE8At%2BF97OT296GffoTMwNlZs6F17J9V3y6OmPvmVPLCTufzd90IlWgV2hOnbfZMK1eFm8k9Zih1ZTfICujCwRdPKih9PdcrjAbZFQS0VlCNQ4MposT8KfWvHa0Vzpxk28Tb9Q0ZQgcjmPYns14CZC%2BzgDxlP%2BAvk%3D; _m_h5_tk=81a26becbdc711f207e9867e9515f45f_1592833369607; _m_h5_tk_enc=b989f2d933cc552ac89899cce03da15d; uc1=cookie14=UoTV7gm1O7Uabg%3D%3D; l=eBEnabfgQrfU91AzBOfwnurza77tLIRAguPzaNbMiOCPO4fM5sHhWZYYDq8HCnGVh6zvR3rEQAfYBeYBqMjnnxvte5DDwQHmn; isg=BNnZ8vR247i3tb_3wSisoUaB6MWzZs0YpC4Jw_uOA4B_AvmUQ7SX6E9YBMZ0umVQnai'
depth = 1  # 爬取的页数

# 获取页面信息
def getHTMLText(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    user_cookies = cookie
    cookies = {}
    for a in user_cookies.split(';'):  # 因为cookies是字典形式，所以用spilt函数将之改为字典形式
        name, value = a.strip().split('=', 1)
        cookies[name] = value
    try:
        r = requests.get(url, cookies=cookies, headers=headers, timeout=60, verify=False)
        print(r.status_code)
        print(r.cookies)
        return r.text
    except Exception as e:
        print(e.args)
        print('获取页面信息失败')
        return ''


# 获取页面信息
def getDetailHTMLText(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    user_cookies = cookie
    cookies = {}
    for a in user_cookies.split(';'):  # 因为cookies是字典形式，所以用spilt函数将之改为字典形式
        name, value = a.strip().split('=', 1)
        cookies[name] = value
    try:
        r = requests.get(url, cookies=cookies, headers=headers, timeout=60, verify=False)
        print(r.status_code)
        print(r.cookies)
        return r.text
    except Exception as e:
        print(e.args)
        print('获取页面詳細信息失败')
        return ''



#  格式化页面，查找数据
def parsePage(html):
    list = []
    try:
        views_title = re.findall('"raw_title":"(.*?)","pic_url"', html)
        print(len(views_title))  # 打印检索到数据信息的个数，如果此个数与后面的不一致，则数据信息不能加入列表
        print(views_title)
        pic_url = re.findall('"pic_url":"(.*?)","detail_url"', html)
        print(len(pic_url))
        views_price = re.findall('"view_price":"(.*?)","view_fee"', html)
        print(len(views_price))
        print(views_price)
        item_loc = re.findall('"item_loc":"(.*?)","view_sales"', html)
        print(len(item_loc))
        print(item_loc)
        views_sales = re.findall('"view_sales":"(.*?)","comment_count"', html)
        print(len(views_sales))
        print(views_sales)
        comment_count = re.findall('"comment_count":"(.*?)","user_id"', html)
        print(len(comment_count))
        print(comment_count)
        shop_name = re.findall('"nick":"(.*?)","shopcard"', html)
        print(len(shop_name))
        nid = re.findall('"nid":"(.*?)","category"', html)
        print(len(shop_name))
        for i in range(len(views_price)):
            list.append([views_title[i],pic_url[i], views_price[i], item_loc[i], comment_count[i], views_sales[i], shop_name[i],nid[i]])
        print('爬取数据成功')
        return list
    except:
        print('有数据信息不全，如某一页面中某一商品缺少地区信息')


def download_image(list):
    for i in range(len(list)):
        spu=list[i]
        spuName = spu[0]
        imageUrl = 'http:'+spu[1]
        file_path = 'D:\\image\\{}.jpg'.format(spuName)
        if not os.path.exists(file_path):
            urllib.request.urlretrieve(imageUrl,file_path)

def list_to_dict(list):
    second_dict = dict()
    first_dict = dict()
    keys = ['name', 'image', 'price', 'loc', 'comment_count', 'sales', 'shop_name']
    for i in range(len(list)):
        for y in range(len(keys)):
            second_dict[keys[y]] = list[i][y]
        first_dict[str(i)] = str(second_dict)
    return first_dict


def getHTMLDetail(list):
    htmls = []

    url = 'https://detail.tmall.com/item.htm?id='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    user_cookies = cookie
    cookies = {}
    for a in user_cookies.split(';'):  # 因为cookies是字典形式，所以用spilt函数将之改为字典形式
        name, value = a.strip().split('=', 1)
        cookies[name] = value
    try:
        for i in range(len(list)):
            spu=list[i]
            detail_url = url+spu[7]
            r = requests.get(detail_url, cookies=cookies, headers=headers, timeout=60, verify=False)
            print(r.status_code)
            print(r.cookies)
            return r.text
    except Exception as e:
        print(e.args)
        print('获取页面信息失败')
        return ''
    return

def get_list(ingoods):
    start_url = 'http://s.taobao.com/search?q=' + ingoods  # 初始搜索地址
    for i in range(depth):
        time.sleep(3 + i)
        try:
            page = i + 1
            print('正在爬取第%s页数据' % page)
            url = start_url + '&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200702&ie=utf8&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s=' + str(
                50 * i)
            print(url)
            html = getHTMLText(url)
            list = parsePage(html)

            html_detail = getHTMLDetail(list)
            return list
        except Exception as e:
            print('获取数据失败')


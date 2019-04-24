import jsonpath
import json
from lxml import etree
import requests
import json
import jsonpath
import os
def getHTML(url):
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    response=requests.get(url,headers=header)
    response.encoding='utf-8'
    html=response.text
    tree=etree.HTML(html)
    sing_id= tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    song_name=tree.xpath('//ul[@class="f-hide"]/li/a/text()')
    # print(song_name)
    for index,i in enumerate(sing_id):
        a=i.split('?')[1]
        b=song_name[index]
        Outer_chain_url='http://music.163.com/song/media/outer/url?%s'%a
        root='E:/python/'
        path = '%s.mp3' % b
        if not os.path.exists(root):
            os.mkdir(root)
        with open (root+path,'wb') as f:
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
            }
            r = requests.get(Outer_chain_url, headers=header)
            f.write(r.content)
            print(b)
def get_Sing_List(urla):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    response1 = requests.get(urla, headers=header)
    response1.encoding = 'utf-8'
    html1 = response1.text
    tree = etree.HTML(html1)
    singer_id = tree.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/@href')
    sing_name = tree.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/text()')
    dicta = dict(zip(sing_name, singer_id))
    input_name=input('现在输入歌手名字')
    if input_name in dicta:
        print('现在开始下载歌曲')
        url = 'https://music.163.com/artist?id=%s' % dicta[input_name].split('=')[1]
        getHTML(url)
    else:
        print('你搜索的歌手不存在请重新输入')
        acquire_sing()
def acquire_sing():
    a = [1001,1002,1003,2001,2002,2003,6001,6002,6003,7001,7002,7003]
    words = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "70", "G": "71", "H": "72", "I": "73",
             "J": "74", "K": "75", "L": "76", "M": "77", "N": "78", "O": "79", "P": "80", "Q": "81", "R": "82",
             "S": "83", "T": "84", "U": "85", "V": "86", "W": "87", "X": "88", "Y": "89", "Z": "90"}
    name = input( '中国(男歌手(0),女歌手(1),组合/乐队(2))\n'
                  '欧美(男歌手(3),女歌手(4),组合/乐队(5))\n'
                  '日本(男歌手(6),女歌手(7),组合/乐队(8))\n'
                  '韩国(男歌手(9),女歌手(10),组合/乐队(11))\n'
                  )
    word = input('请输入歌手首字母(注意是大写)')
    url = 'https://music.163.com/discover/artist/cat?id=%s&initial=%s' % (a[int(name)], words[word])
    print(url)
    get_Sing_List(url)
acquire_sing()
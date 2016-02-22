__author__ = 'shadowmydx'
'''
POST /weapi/song/enhance/player/url?csrf_token= HTTP/1.1
Host: music.163.com
Proxy-Connection: keep-alive
Content-Length: 390
Origin: http://music.163.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Referer: http://music.163.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: visited=true;
'''


def get_header():
    header = dict()
    header['Host'] = 'music.163.com'
    header['Origin'] = 'http://music.163.com'
    header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'
    header['Content-Type'] = 'application/x-www-form-urlencoded'
    header['Accept'] = '*/*'
    header['Referer'] = 'http://music.163.com'
    header['Accept-Encoding'] = 'gzip, deflate'
    header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
    header['Cookie'] = 'visited=true;'
    return header

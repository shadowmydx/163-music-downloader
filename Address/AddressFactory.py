# -*- coding:utf-8 -*-
import HeaderFactory
from JsFactory import ParamFactory
import urllib
import urllib2
import gzip
import json
from StringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('utf8')
__author__ = 'shadowmydx'


class AddressFactory:

    def __init__(self):
        self.factory = ParamFactory.ParamFactory()
        self.url = r'http://music.163.com/weapi/song/enhance/player/url?csrf_token='
        self.headers = HeaderFactory.get_header()

    def get_music_address(self, ids):
        enc_tuple = self.factory.get_params(ids) # 116871
        payload = {'params': enc_tuple[0], 'encSecKey': enc_tuple[1]}
        payload = urllib.urlencode(payload)
        req = urllib2.Request(url=self.url, headers=self.headers, data=payload)
        response = urllib2.urlopen(req)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
            data = json.loads(data)
            try:
                print 'Get address of song ' + ids
                return data['data'][0]['url']
            except:
                print ids
                return None

if __name__ == '__main__':
    address = AddressFactory()
    print address.get_music_address('116871')

# -*- coding:utf-8 -*-
import urllib2
import re
import os
import string
from Address import AddressFactory
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'shadowmydx'


class AlbumGetter:

    def __init__(self):
        self.url = r'http://music.163.com/album?id=' # 11410
        self.root_folder = '163-music/'
        self.ids = None
        self.album_name = None
        self.limit = 10
        self.address_factory = AddressFactory.AddressFactory()

    def set_album_id(self, ids):
        self.ids = ids

    def set_root_folder(self, folder):
        self.root_folder = folder

    def build_music_folder(self):
        if os.path.isdir(self.root_folder + self.album_name):
            return
        self.album_name = self.album_name.split('/')[0].strip()
        os.makedirs(self.root_folder.strip() + self.album_name)

    def download_album(self):
        true_url = self.url + self.ids
        content_file = urllib2.urlopen(true_url)
        content = content_file.read()
        self.album_name = self.get_album_name(content)
        all_music = self.get_all_music(content)
        all_music = self.get_all_music_address(all_music)
        self.build_music_folder()
        self.download_all_music(all_music)
        content_file.close()

    @staticmethod
    def format_filename(filename):
        illegal = u'<>:"\|?*'
        for item in illegal:
            filename = filename.replace(item, '_')
        return filename

    @staticmethod
    def pre_url_handle(file_url):
        return file_url.replace("http://", "http://183.6.245.250/")

    def download_all_music(self, all_music):
        for item in all_music:
            file_name = item[1]
            file_url = item[2]
            retry = 0
            target = None
            while retry < self.limit:
                try:
                    file_url = self.pre_url_handle(file_url)
                    target = urllib2.urlopen(file_url)
                    break
                except:
                    print 'Net error, try again...'
                    retry += 1
            file_name = unicode(self.root_folder + self.album_name + '/' + file_name + '.mp3')
            file_name = self.format_filename(file_name)
            local = open(file_name, 'wb')
            local.write(target.read())
            print 'downloading ' + file_name + ' finished.'
            local.close()

    def get_all_music_address(self, all_music):
        result = list()
        for item in all_music:
            address = self.address_factory.get_music_address(item[0])
            if address is not None:
                result.append((item[0], item[1], address))
        return result

    @staticmethod
    def get_album_name(content):
        title_pat = re.compile(r'<h2 class="f-ff2">(?P<title>.*?)</h2>', re.DOTALL)
        match = title_pat.search(content)
        return unicode(match.group('title'))

    @staticmethod
    def get_all_music(content):
        music_pat = re.compile(r'<a href="/song\?id=(?P<ids>\d*?)">(?P<name>.*?)</a>', re.DOTALL)
        matches = music_pat.findall(content)
        return matches


if __name__ == '__main__':
    album = AlbumGetter()
    album.set_album_id('46922')
    album.download_album()
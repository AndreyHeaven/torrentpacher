import ini
#! /usr/bin/python
from inifile import INIFile
from time import sleep
import bencode
import time
import tp_config
import datetime
import os
__author__="araygorodskiy"
__date__ ="$24.02.2009 14:52:22$"
class Deamon(object):
    def __init__(self):
        self.config = tp_config.get_file();
        self.from_dir = self.config.get('deamon','from_dir');
        self.to_dir = self.config.get('deamon','to_dir');
        self.city_number = int(self.config.get('config','city'));
        self.prov_number = int(self.config.get('config','provider'));
        self.last_update_time=0.0
        self.ini = INIFile();

    def exec_transform(self):
        files = os.listdir(self.from_dir)
        args = []
        for f in files:
            name, ext = os.path.splitext(f)
            if ext == ".torrent":
                args.append(os.path.join(self.from_dir, f))
        for torr in args:
            modif_time = os.stat(torr).st_mtime
            if modif_time > self.last_update_time:
                print "Update time = %s" % self.last_update_time
                print "Accept %s" % torr
                urls = self.ini.get_urls_for_city_and_prov(self.city_number,self.prov_number);
                bencode.add_URLs_to_torrent(args,urls,self.to_dir);
                os.utime(torr, (time.time(),time.time()))

    def repeat(self):
        while True:
            self.last_update_time=time.time();
            print "Update time = %s" % self.last_update_time
            self.exec_transform()
            sleep(1)


if __name__ == "__main__":
    Deamon().repeat()

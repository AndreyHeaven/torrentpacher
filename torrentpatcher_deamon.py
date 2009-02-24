#! /usr/bin/python
import tp_config;
import threading;

__author__="araygorodskiy"
__date__ ="$24.02.2009 14:52:22$"
config = tp_config.get_file();
from_dir = config.get('deamon','from_dir');
to_dir = config.get('deamon','to_dir');

def exec_transform():
    print 'hello'

def repeat():
    t = threading.Timer(1.0,exec_transform);
    t.start();

if __name__ == "__main__":
    repeat()

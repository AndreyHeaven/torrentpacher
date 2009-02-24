# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="araygorodskiy"
__date__ ="$19.02.2009 11:21:25$"
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('tp.cfg')

def get_config():
    return config.items('config')

def get_file():
    return config

def set_config(items):
    for i,a in items:
        config.set('config',i,a);
    configfile = open('tp.cfg', 'wb');
    config.write(configfile)
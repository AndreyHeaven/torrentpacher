#!/usr/bin/env python

from bencode import add_URLs_to_torrent
import ini
import os
import sys;
from inifile import *;
import getopt;
__author__="araygorodskiy"
__date__ ="$18.02.2009 14:36:25$"
try:
    ini = INIFile();
except:
    os.system('sh ./update_tracker_list');
def help():
    print "--help This help\n-c City number use \"help\" for list\n-p Provider number use \"help\" for list, use with city number\n--update Update retracker list"

def print_cites():
    print "Cites and its numbers:"
    for i in ini.cites:
        print "\t",i, ini.cites[i].name;
def print_providers(city):
    print "Providers for "+ini.cites[city].name;
    for i in ini.cites[city].providers:
        print "\t",i, ini.cites[city].providers[i].name;
if __name__ == "__main__":
    args = sys.argv[1:]
    optlist, args = getopt.getopt(args, 'hc:p:',["help","update"])
    city_number = 0;
    prov_number = 0;
    for o, a in optlist:
        if o == "-c":
            if (a == "help"):
                print_cites();
                sys.exit();
            else:
                city_number = int(a);
        elif o == "-p":
            if (a == "help"):
                if city_number != 0:
                    print_providers(city_number);
                    sys.exit();
                else:
                    print "You must specify City"
                    sys.exit();
            else:
                prov_number = int(a);
        elif o in ("-h", "--help"):
            help();
            sys.exit();
        elif o == "--update":
            os.system('sh ./update_tracker_list');
            sys.exit();
        else:
            assert False, "unhandled option"
    if city_number == 0 or prov_number == 0 or len(args) == 0:
        print "Something wrong!!!"
        help();
        sys.exit(2);

    for arg in args:
        if not os.path.exists(arg):
            print "%s not exists!" % arg
            help();
            sys.exit(2);
        if os.path.isdir(arg):
            args.remove(arg)
            for f in os.listdir(arg):
                name, ext = os.path.splitext(f)
                if ext == ".torrent":
                    args.append(os.path.join(arg, f))


    urls = ini.get_urls_for_city_and_prov(city_number,prov_number);
    add_URLs_to_torrent(args,urls);

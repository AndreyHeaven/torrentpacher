#!/usr/bin/env python

from bencode import add_URLs_to_torrent
import ini
import sys;
from inifile import *;
import getopt;
__author__="araygorodskiy"
__date__ ="$18.02.2009 14:36:25$"
ini = INIFile("trackerssimple-utf8.ini");
def help():
    print "--help This help\n-c City number use \"help\" for list\n-p Provider number use \"help\" for list, use with city number"

def print_cites():
    print "Cites and its numbers:"
    for i in ini.cites:
        print "\t",i, ini.cites[i].name;
def print_providers(city):
    print "Providers for "+ini.cites[city].name;
    for i in ini.cites[city].providers:
        print "\t",i, ini.cites[city].providers[i].name;
def get_urls_for_city_and_prov(city,prov):
    return ini.cites[city].providers[prov].re_trackers.values();
if __name__ == "__main__":
    args = sys.argv[1:]
    optlist, args = getopt.getopt(args, 'hc:p:',["help"])
    if len(optlist) == 0 or len(args)==0:
        help();
        sys.exit();
    for i in optlist:
        if "--help" in i:
            help();
            sys.exit();
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
        else:
            assert False, "unhandled option"
    if city_number == 0 or prov_number == 0 or len(args) == 0:
        print "Something wrong!!!"
        help();
        sys.exit(2);

    urls = get_urls_for_city_and_prov(city_number,prov_number);
    add_URLs_to_torrent(args,urls);

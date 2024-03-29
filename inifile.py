#!/usr/bin/python
# -*- coding: utf-8 -*-
from ini import INIConfig
# To change this template, choose Tools | Templates
# and open the template in the editor.
GOROD = "Город";
KOLVO = "Количество";
PROVIDERS = "Провайдеры ";
RE_TRACKERS = "Ретрекеры ";
class Provider(object):
    def __str__( self ):
        return self.name + ": " + str(self.re_trackers);
    def __init__(self, name, re_trackers):
        self.name = name;
        self.re_trackers = re_trackers;

class City(object):
    def __str__(self):
        return self.name + ": " + str(self.providers);
    def __init__(self, name, providers):
        self.name = name;
        self.providers = providers;

class INIFile(object):
    def __init__(self):
        config = INIConfig(open('trackerssimple-utf8.ini'));
        self.cites = {};
        size = config[GOROD][KOLVO];
        for i in range(1, int(size)+1):
            name = config[GOROD][str(i)]
            providers = self._get_providers(config, name);

            city = City(name, providers);
            self.cites[i] = city

    def get_urls_for_city_and_prov(self, city, prov):
        return self.cites[city].providers[prov].re_trackers.values();

    def _get_providers(self, config, name):
        provs = {};
        size = config[PROVIDERS + name][KOLVO];
        for i in range(1, int(size)+1):
            name1 = config[PROVIDERS + name][str(i)];
            re_trackers = self._get_re_trackers(config, name, name1);
            provs[i] = Provider(name1, re_trackers)
        return provs;

    def _get_re_trackers(self, config, city, provider):
        tr = {};
        size = config[RE_TRACKERS + city + " " + provider][KOLVO];
        for i in range(1, int(size)+1):
            url = config[RE_TRACKERS + city + " " + provider][str(i)];
            tr[i] = url;
        return tr;


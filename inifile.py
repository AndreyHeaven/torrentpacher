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

class INIFile:
    def __init__(self, file_name):
        config = INIConfig(open(file_name));
        self.cites = {};
        size = config[GOROD][KOLVO];
        for i in range(1, int(size)):
            name = config[GOROD][str(i)]
            providers = self._get_providers(config, name);

            city = City(name, providers);
            self.cites[i] = city

    def _get_providers(self, config, name):
        provs = {};
        size = config[PROVIDERS + name][KOLVO];
        for i in range(1, int(size)):
            name1 = config[PROVIDERS + name][str(i)];
            re_trackers = self._get_re_trackers(config, name, name1);
            provs[i] = Provider(name1, re_trackers)
        return provs;

    def _get_re_trackers(self, config, city, provider):
        tr = {};
        size = config[RE_TRACKERS + city + " " + provider][KOLVO];
        for i in range(1, int(size)):
            url = config[RE_TRACKERS + city + " " + provider][str(i)];
            tr[i] = url;
        return tr;


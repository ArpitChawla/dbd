# -*- coding: utf-8 -*-

'''
    Genesis Add-on
    Copyright (C) 2015 ArpitChawla
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import os,sys,re,json,urllib,urlparse,base64,datetime

try: action = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))['action']
except: action = None

from resources.lib.libraries import control
from resources.lib.libraries import client
from resources.lib.libraries import cache
from resources.lib.libraries import metacache
from resources.lib.libraries import favourites
from resources.lib.libraries import workers
from resources.lib.libraries import views

class movies:
    def __init__(self):
        self.list = []
        
        self.cinemalytics_link = 'http://http://api.cinemalytics.com'
        self.cinemalytics_key = '651807C47FBA2DB4CFC242EADAAC10C4'
        self.datetime = (datetime.datetime.utcnow() - datetime.timedelta(hours = 5))
        self.systime = (self.datetime).strftime('%Y%m%d%H%M%S%f')
        self.today_date = (self.datetime).strftime('%Y-%m-%d')
        self.month_date = (self.datetime - datetime.timedelta(days = 30)).strftime('%Y-%m-%d')
        self.month2_date = (self.datetime - datetime.timedelta(days = 60)).strftime('%Y-%m-%d')
        self.year_date = (self.datetime - datetime.timedelta(days = 365)).strftime('%Y-%m-%d')
        self.info_lang = control.setting('infoLang') or 'en'
        
        self.persons_link = 'http://api.cinemalytics.com/v1/person/name/Nawaz/?%s&query=%s'

#!/usr/bin/env python2
#-*- encoding: utf-8 -*-

import sys
reload(sys).setdefaultencoding("utf8")

import urllib
import urllib2
import json

def reply(s):
    try:
        response = urllib2.urlopen("http://www.tuling123.com/openapi/api?key=&info=" + urllib.quote(s.encode("utf8")))
        data = response.read()
        result = json.loads(data)
        re = result['text']
        return re.decode("utf8")
    except:
        return "玩坏掉了。"
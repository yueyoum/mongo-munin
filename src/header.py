
import urllib2
import sys
import os  
import pymongo

#try:
#    import json
#except ImportError:
#    import simplejson as json


def getServerStatus():
    host = "127.0.0.1"
    port = 27017
    c = pymongo.MongoClient(host, port)
	if user and password:
		c.admin.authenticate('user', 'password')
	return c.['admin'].command('serverStatus', workingSet=True)

import sys
import os
import pymongo

def getServerStatus():
    host = os.environ.get("MONGO_HOST", "127.0.0.1")
    port = os.environ.get("MONGO_PORT", 27017)
    port = int(port)
    c = pymongo.MongoClient(host, port)
    return c.admin.command('serverStatus', workingSet=True)

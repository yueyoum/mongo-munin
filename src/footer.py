
if __name__ == "__main__":          
	
    from os import environ
    if 'HOST' in environ:
        host = environ['HOST']
    if 'PORT' in environ:
        port = environ['PORT']
    if 'USER' in environ:
        user = environ['USER']
    if 'PASSWORD' in environ:
        password = environ['PASSWORD']
    
if len(sys.argv) > 1 and sys.argv[1] == "config":
    doConfig()
else:
    doData()


def doData():
    ss = getServerStatus()
    print "pagefaults.value", ss['extra_info']['page_faults']

def doConfig():

    print "graph_title MongoDB Page Faults"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel page faults"
    print "graph_category MongoDB"

    print "pagefaults.label page faults"
    print "pagefaults.min 0"
    print "pagefaults.draw LINE1"

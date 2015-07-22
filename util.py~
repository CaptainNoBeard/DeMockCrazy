import urllib2
import json

def get_votes_GOP():
    urlGOP = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-gop-primary'
    uGOP = urllib2.urlopen( urlGOP )
    resultGOP = json.loads(uGOP.read())
    resultGOP = resultGOP[0:1]
    return resultGOP[0]['estimates'][0]
    
def get_votes_DEM():
    urlDEM = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-dem-primary'
    uDEM = urllib2.urlopen( urlDEM )
    resultDEM = json.loads(uDEM.read())
    resultDEM = resultDEM[0:1]
    return resultDEM[0]['estimates'][0]

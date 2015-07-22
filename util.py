import urllib2
import json

def get_votes():
    urlGOP = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-gop-primary'
    uGOP = urllib2.urlopen( urlGOP )
    resultGOP = json.loads(uGOP.read())
    resultGOP = resultGOP[0:1]
    return resultGOP[0]['estimates'][0]['value']
    ################return result['list'][0]['main']['votes']

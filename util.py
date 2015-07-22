import urllib2
import json
import unicodedata

def get_votes_GOP():
    urlGOP = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-gop-primary'
    uGOP = urllib2.urlopen( urlGOP )
    resultGOP = json.loads(uGOP.read())
    resultGOP = resultGOP[0:1][0]['estimates'][0]
    pts = str(resultGOP['value'])
    name = str(resultGOP['first_name']) + ' ' + str(resultGOP['last_name'])
    party = str(resultGOP['party'])
    leadGOP = name + ' is in the lead of the ' + party +' primary race, with '+ pts + ' percent of the ' + party + ' vote.'
    return leadGOP
    
def get_votes_DEM():
    urlDEM = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-dem-primary'
    uDEM = urllib2.urlopen( urlDEM )
    resultDEM = json.loads(uDEM.read())
    resultDEM = resultDEM[0:1][0]['estimates'][0]
    pts = str(resultDEM['value'])
    name = str(resultDEM['first_name']) + ' ' + str(resultDEM['last_name'])
    party = str(resultDEM['party'])
    leadDEM = name + ' is in the lead of the ' + party +' primary race, with '+ pts + ' percent of the ' + party + ' vote.'
    return leadDEM

def results():
    print get_votes_GOP(), get_votes_DEM()
##    lead = leadGOP + leadDEM
##    print lead

import urllib2
import json
import unicodedata

def get_votes_GOP():
    urlGOP = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-gop-primary'
    uGOP = urllib2.urlopen( urlGOP )
    resultGOP = json.loads(uGOP.read())
    resultGOP = resultGOP[0:1][0]['estimates'][0]
    pts = str(resultGOP['value'])
    gopName = str(resultGOP['first_name']) + ' ' + str(resultGOP['last_name'])
    party = str(resultGOP['party'])
    leadGOP = gopName + ' is in the lead of the Republican primary race, with '+ pts + ' percent of the Republican vote.'
    return leadGOP
    
def get_votes_DEM():
    urlDEM = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-dem-primary'
    uDEM = urllib2.urlopen( urlDEM )
    resultDEM = json.loads(uDEM.read())
    resultDEM = resultDEM[0:1][0]['estimates'][0]
    pts = str(resultDEM['value'])
    demName = str(resultDEM['first_name']) + ' ' + str(resultDEM['last_name'])
    party = str(resultDEM['party'])
    leadDEM = demName + ' is in the lead of the Democratic primary race, with '+ pts + ' percent of the Democratic vote. \n'
    return leadDEM

def results():
    return get_votes_DEM() + get_votes_GOP()
    
def get_name_GOP():
    urlGOP = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-gop-primary'
    uGOP = urllib2.urlopen( urlGOP )
    resultGOP = json.loads(uGOP.read())
    resultGOP = resultGOP[0:1][0]['estimates'][0]
    gopName = str(resultGOP['first_name']) + ' ' + str(resultGOP['last_name'])
    return gopName

def get_name_DEM():
    urlDEM = 'http://elections.huffingtonpost.com/pollster/api/charts.json?topic=2016-president-dem-primary'
    uDEM = urllib2.urlopen( urlDEM )
    resultDEM = json.loads(uDEM.read())
    resultDEM = resultDEM[0:1][0]['estimates'][0]
    demName = str(resultDEM['first_name']) + ' ' + str(resultDEM['last_name'])
    return demName

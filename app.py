from flask import Flask, render_template, request
from util import *
import datetime
import urllib2
from urllib import urlencode

try:
    import json
except ImportError:
    import simplejson as json


app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def root(): 
    gopName = get_name_GOP()
    demName = get_name_DEM()
    return render_template('index.html', demResults=get_votes_DEM(), gopResults=get_votes_GOP(), gopName=gopName, demName=demName)
    
if __name__ == '__main__':
    app.debug = True
    app.run( port = 4269 )

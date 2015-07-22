from flask import Flask, render_template, request
import util
import datetime
import urllib2
from urllib import urlencode

try:
    import json
except ImportErorr:
    import simplejson as json


app = Flask( __name__ )

@app.route('/', methods=["GET","POST"])
def root( ):
    if request.method=="POST":
        print result




if __name__ == '__main__':
    app.debug = True
    app.run( port = 42069 )

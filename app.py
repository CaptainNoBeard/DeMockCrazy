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
    return results()


if __name__ == '__main__':
    app.debug = True
    app.run( port = 4209 )

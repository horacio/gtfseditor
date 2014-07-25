#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bottle import static_file, route
from server import app

# @route('/:file#(favicon.ico|humans.txt)#')
# def favicon(file):
#   return static_file(file, root='project/static/misc')

# @route('/:path#(images|css|js|fonts)\/.+#')
# def server_static(path):
#   return static_file(path, root='project/static')

@app.get('/api/kml/')
def kmlFiles():
  options = []
  for filename in sorted(os.listdir('./app/kml')):
    options.append({'value': filename})
  return {'options': options}

@app.get('/bower_components/<filepath:path>')
def server_files(filepath):
  return static_file(filepath, root='./bower_components/')

@app.get('/<filepath:path>')
def index(filepath):
  return static_file(filepath, root='./app/')

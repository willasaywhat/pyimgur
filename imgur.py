#!/bin/env python

__author__ = 'Devon Meunier <devon.meunier@myopicvoid.org>'
__description__ = "A Pythonic interface to the imgur api."

import simplejson
import pycurl
import StringIO

class imgurAPIError(Exception):
  pass

class imgur:
  def __init__(self, apikey=None):
    self.apikey = apikey
    self.FILE = pycurl.FORM_FILE

  def upload(self, image):
    if self.apikey is None:
      raise imgurAPIError, "API Key is missing."
      return -1
    else:
      out = StringIO.StringIO()
      c = pycurl.Curl()
      values = [("key", self.apikey),
                ("image", image),
               ]
      c.setopt(pycurl.URL, "http://imgur.com/api/upload.json")
      c.setopt(pycurl.HTTPPOST, values)
      c.setopt(pycurl.WRITEFUNCTION, out.write)
      c.perform()
      c.close()

      return simplejson.loads(out.getvalue())

  def delete(self, dhash):
    c = pycurl.Curl()
    out = StringIO.StringIO()
    c.setopt(pycurl.URL, "http://imgur.com/api/delete/%s.json" % dhash)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.WRITEFUNCTION, out.write)
    c.perform()
    c.close()
    
    return simplejson.loads(out.getvalue())

  def istats(self, ihash):
    out = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "http://imgur.com/api/stats/%s.json" % ihash)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.WRITEFUNCTION, out.write)
    c.perform()
    c.close()

    return simplejson.loads(out.getvalue())

  def stats(self, view="all"):
    out = StringIO.StringIO()
    c = pycurl.Curl()
    values = [("view", view)]
    c.setopt(pycurl.URL, "http://imgur.com/api/stats.json")
    c.setopt(pycurl.HTTPPOST, values)
    c.setopt(pycurl.WRITEFUNCTION, out.write)
    c.perform()
    c.close()

    return simplejson.loads(out.getvalue())

  def gallery(self, sort="latest", view="all", count=20, page=1):
    out = StringIO.StringIO()
    values = [("sort", sort),
              ("view", view),
              ("count", count),
              ("page", page),
             ]
    c.setopt(pycurl.URL, "http://imgur.com/api/gallery.json")
    c.setopt(pycurl.HTTPPOST, values)
    c.setopt(pycurl.WRITEFUNCTION, out.write)
    c.perform()
    c.close()

    return simplejson.loads(out.getvalue())

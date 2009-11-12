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

  def upload(self, image):
    if self.apikey is None:
      raise imgurAPIError, "API Key is missing."
      return -1
    else:
      c = pycurl.Curl()
      b = StringIO.StringIO()
      values = [("key", self.apikey),
                ("image", image)]

      c.setopt(c.URL, "http://imgur.com/api/upload.json")
      c.setopt(c.HTTPPOST, values)
      c.setopt(pycurl.WRITEFUNCTION, b.write)
      c.perform()
      c.close()

      return simplejson.loads(b.getvalue())

  def delete(self, dhash):
    c = pycurl.Curl()
    b = StringIO.StringIO()
    c.setopt(pycurl.URL, "http://imgur.com/api/delete/%s.json" % dhash)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.perform()
    c.close()
    
    return simplejson.loads(b.getvalue())

  def istats(self, ihash):
    b = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "http://imgur.com/api/stats/%s.json" % ihash)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.perform()
    c.close()

    return simplejson.loads(b.getvalue())

  def stats(self, view = "all"):
    values = [("view", view)]
    b = StringIO.StringIO()
    c.setopt(pycurl.URL, "http://imgur.com/api/stats.json")
    c.setopt(pycurl.HTTP_POST, values)
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    c.close()

    return simplejson.loads(b.getvalue())

  def gallery(self, sort="latest", view="all" count=20, page=1):
    values = [("sort", sort),
              ("view", view),
              ("count", count),
              ("page", page)]
    b = StringIO.StringIO()
    c.setopt(pycurl.URL, "http://imgur.com/api/gallery.json")
    c.setopt(pycurl.HTTP_POST, values)
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    c.close()

    return simplejson.loads(b.getvalue())

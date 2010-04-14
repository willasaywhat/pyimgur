#!/bin/env python

__author__ = 'Devon Meunier <devon.meunier@myopicvoid.org>'
__description__ = "A Pythonic interface to the imgur api."

import simplejson
import pycurl
import StringIO

FILE = pycurl.FORM_FILE

class imgurAPIError(Exception):
  pass

class imgur:
  def __init__(self, apikey=None):
    self.apikey = apikey

  def upload(self, image):
    """
    Upload an image to imgur.
    'image' Must be in the form (imgur.FILE, "/path/to/file")
    Returns the parsed json that imgur returns.
    """
    if self.apikey is None:
      raise imgurAPIError, "API Key is missing."
      return None 
    else:
      out = StringIO.StringIO()
      c = pycurl.Curl()
      values = [("key", self.apikey),
                ("image", (c.FORM_FILE,image)),
               ]
      c.setopt(pycurl.URL, "http://imgur.com/api/upload.json")
      c.setopt(pycurl.HTTPPOST, values)
      c.setopt(pycurl.WRITEFUNCTION, out.write)
      c.perform()
      c.close()

      return simplejson.loads(out.getvalue())

  def upload_from_url(self, image):
    """
    Upload an image to imgur.
    'image' must be a URL
    Returns the parsed json that imgur returns.
    """
    if self.apikey is None:
      raise imgurAPIError, "API Key is missing."
      return None
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
    """
    Delete an image from imgur.
    dhash is the delete hash found in the object returned by a call to
     imgur.upload
    Returns the parsed json that imgur returns.
    """
    c = pycurl.Curl()
    out = StringIO.StringIO()
    c.setopt(pycurl.URL, "http://imgur.com/api/delete/%s.json" % dhash)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.WRITEFUNCTION, out.write)
    c.perform()
    c.close()
    
    return simplejson.loads(out.getvalue())

  def istats(self, ihash):
    """
    Returns the image's stats corresponding to its hash, ihash.
    """
    out = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "http://imgur.com/api/stats/%s.json" % ihash)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.WRITEFUNCTION, out.write)
    c.perform()
    c.close()

    return simplejson.loads(out.getvalue())

  def stats(self, view="all"):
    """
    Returns imgur statistics.
    """
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
    """
    Returns the stats of several images from the imgur database.
    There is no way to specify which images are returned.
    """
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

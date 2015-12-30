"""

process.keg

"""


import config

import process

import model

from google.appengine.ext import ndb


class KegNotFound(process.util.ProcessorException):
  pass


class KegDependencyProcessor(process.util.AbstractProcessor):
  def __init__(self, *args, **kwargs):
    if 'keg_id' not in kwargs:
      raise process.util.ProcessorException("`keg_id` missing from kwargs")
    self.keg_id = kwargs.get('keg_id')
    super(KegDependencyProcessor, self).__init__(*args, **kwargs)

  @property
  def keg(self, *args, **kwargs):
      if not hasattr(self, 'keg_id'):
        raise process.util.ProcessorException("self has not `keg_id` property")
      key = ndb.Key(model.Keg, self.keg_id)
      self._keg = key.get()
      if type(self._keg) is not model.Keg:
        raise KegNotFound("keg_id")
      return self._keg


class KegObjectProcessor(KegDependencyProcessor):
  def process(self, *args, **kwargs):
    self.response_object = self.keg.json_object


class KegCreateProcessor(process.util.AbstractProcessor):
  def process(self, *args, **kwargs):
    if 'name' not in kwargs:
      raise process.util.ProcessorException("`name` missing from kwargs")
    keg = model.Keg.create(kwargs.get('name'), self.user,
      unit=kwargs.get('unit'),
      capacity=kwargs.get('capacity'),
      consumed=kwargs.get('consumed'))
    self.response_object = keg.json_object


class KegListProcessor(process.util.AbstractProcessor):
  def process(self, *args, **kwargs):
    query = model.Keg.query(model.Keg.users == self.user.key)
    kegs = query.fetch()
    for keg in kegs:
      self.response_list.append(keg.json_object)


class KegUpdateProcessor(KegDependencyProcessor):
  def process(self, *args, **kwargs):
    if 'name' in kwargs:
      self.keg.name = kwargs.get('name')
    if 'capacity' in kwargs:
      self.keg.capacity = kwargs.get('capacity')
    if 'consumed' in kwargs:
      self.keg.consumed = kwargs.get('consumed')
    if 'unit' in kwargs:
      self.keg.unit = kwargs.get('unit')
    self.keg.put()
    self.response_object = self.keg.json_object

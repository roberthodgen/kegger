"""

model.keg

"""


from google.appengine.ext import ndb

import model

import config

from ndb_users import users


class Unit:
  OUNCE = 'oz'
  MILLILITER = 'ml'
  LITER = 'l'


class KegCreateException(model.util.ModelException):
  pass


class KegGetException(model.util.ModelException):
  pass


class Keg(ndb.Model):
  name = ndb.StringProperty(required=True)
  users = ndb.KeyProperty(repeated=True, kind=users.User)
  capacity = ndb.FloatProperty(default=0)
  consumed = ndb.FloatProperty(default=0)
  unit = ndb.StringProperty(required=True,
    choices=[Unit.OUNCE, Unit.MILLILITER, Unit.LITER], default=Unit.OUNCE)
  brewerdb_id = ndb.StringProperty(default=None)
  style = ndb.StringProperty(default=None)
  description = ndb.StringProperty(indexed=False)
  ibu = ndb.IntegerProperty(default=None)
  abv = ndb.FloatProperty(default=None)
  glass = ndb.StringProperty(default=None)
  image = ndb.StringProperty(default=None)
  created = ndb.DateTimeProperty(auto_now_add=True)
  updated = ndb.DateTimeProperty(auto_now=True)

  @classmethod
  def create(cls, name, user, **kwargs):
    if type(user) is not users.User:
      raise KegCreateException("user not instance of User")
    if len(name) < config.KEG_NAME_MIN_LEN:
      raise KegCreateException("name too short")
    unit = kwargs.get('unit', None)
    if unit is None:
      unit = Unit.OUNCE
    keg = cls(name=name, unit=unit)
    keg.users.append(user.key)
    if 'consumed' in kwargs and kwargs.get('consumed') is not None:
      keg.consumed = float(kwargs.get('consumed'))
    if 'capacity' in kwargs and kwargs.get('capacity') is not None:
      keg.capacity = float(kwargs.get('capacity'))
    if 'brewerdb_id' in kwargs and kwargs.get('brewerdb_id') is not None:
      keg.brewerdb_id = kwargs.get('brewerdb_id')
    if 'style' in kwargs and kwargs.get('style') is not None:
      keg.style = kwargs.get('style')
    if 'description' in kwargs and kwargs.get('description') is not None:
      keg.description = kwargs.get('description')
    if 'ibu' in kwargs and kwargs.get('ibu') is not None:
      keg.ibu = int(kwargs.get('ibu'))
    if 'abv' in kwargs and kwargs.get('abv') is not None:
      keg.abv = float(kwargs.get('abv'))
    if 'glass' in kwargs and kwargs.get('glass') is not None:
      keg.glass = kwargs.get('glass')
    if 'image' in kwargs and kwargs.get('image') is not None:
      keg.image = kwargs.get('image')
    if keg.put():
      return keg
    raise KegCreateException("put fail")

  @classmethod
  def get(cls, keg_id, user):
    if type(user) is not users.User:
      raise KegGetException("user not instance of User")
    key = ndb.Key(cls, keg_id)
    keg = key.get()
    if type(keg) is not cls:
      return None
    if user.key not in keg.users:
      return None
    return keg

  @property
  def created_utc(self):
    """ Return `created` with tzinfo set to `UTC`. """
    return self.created.replace(tzinfo=config.utc_tz)

  @property
  def updated_utc(self):
    """ Return `updated` with tzinfo set to `UTC`. """
    return self.updated.replace(tzinfo=config.utc_tz)

  @property
  def json_object(self):
    """ Return a JSON-encodable dict for this class. """
    json_object = {
      'name': self.name,
      'capacity': self.capacity,
      'consumed': self.consumed,
      'unit': self.unit,
      'created': self.created_utc.isoformat(),
      'updated': self.updated_utc.isoformat(),
      'brewerdb_id': self.brewerdb_id,
      'style': self.style,
      'description': self.description,
      'ibu': self.ibu,
      'abv': self.abv,
      'glass': self.glass,
      'image': self.image,
      'id': self.key.id()
    }
    return json_object

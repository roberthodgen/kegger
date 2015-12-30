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


class Keg(ndb.Model):
  name = ndb.StringProperty(required=True)
  users = ndb.KeyProperty(repeated=True, kind=users.User)
  capacity = ndb.FloatProperty(default=0)
  consumed = ndb.FloatProperty(default=0)
  unit = ndb.StringProperty(required=True,
    choices=[Unit.OUNCE, Unit.MILLILITER, Unit.LITER], default=Unit.OUNCE)
  created = ndb.DateTimeProperty(auto_now_add=True)
  updated = ndb.DateTimeProperty(auto_now=True)

  @classmethod
  def create(cls, name, user, unit=Unit.OUNCE):
    if type(user) is not users.User:
      raise KegCreateException("user not instance of User")
    if len(name) < config.KEG_NAME_MIN_LEN:
      raise KegCreateException("name too short")
    keg = cls(name=name)
    keg.users.append(user.key)
    if keg.put():
      return keg
    raise KegCreateException("put fail")

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
      'id': self.key.id()
    }
    return json_object

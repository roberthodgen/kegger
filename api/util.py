"""

util

"""


from datetime import tzinfo, timedelta


class UTC(tzinfo):
    """ Defines a `tzinfo` subclass for UTC/Universal Coordindated Time.
    All dates are stored in NDB without time zone information. This UTC class
    is needed so `datetime.isoformat()` includes timezone information. """

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)

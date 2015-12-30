"""

process.util

"""


from ndb_users import users


class AbstractProcessor(object):
    def __init__(self, *args, **kwargs):
        self.response_object = dict()
        self.response_list = list()
        self.process(*args, **kwargs)

    @property
    def user(self):
        return users.get_current_user()


class ProcessorException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

"""

process.status

"""


import process.util

import config

from datetime import datetime


class StatusProcessor(process.util.AbstractProcessor):
  def process(self, *args, **kwargs):
    timestamp = datetime.now()
    timestamp = timestamp.replace(tzinfo=config.utc_tz)
    self.response_object['timestamp'] = timestamp.isoformat()
    self.response_object['up'] = True
    self.response_object['user'] = dict()
    self.response_object['user']['email'] = self.user.email

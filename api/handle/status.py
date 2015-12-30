"""

handle.status

"""


import handle.util

import process

import json


class StatusRequestHandler(handle.util.AbstractRequestHandler):
  def get(self):
    self.verify_user()
    processor = process.StatusProcessor()
    self.response.content_type = 'application/json'
    self.response.out.write(json.dumps(processor.response_object))

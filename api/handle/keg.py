"""

handle.keg

"""


import config

import handle

import json

import process


class KegRequestHandler(handle.util.AbstractRequestHandler):
  def post(self):
    self.verify_user()
    self.load_request()
    self.post_validate()
    processor = process.KegCreateProcessor(**self.request_object)
    self.response.content_type = 'application/json'
    self.response.out.write(json.dumps(processor.response_object))

  def post_validate(self):
    if 'name' not in self.request_object:
      raise handle.util.InputMissingRequestException("name")

  @handle.util.param([('keg_id', int)])
  def get(self, **kwargs):
    self.verify_user()
    if self.keg_id:
      processor = process.KegObjectProcessor(keg_id=self.keg_id)
      self.response.content_type = 'application/json'
      self.response.out.write(json.dumps(processor.response_object))
    else:
      processor = process.KegListProcessor()
      self.response.content_type = 'application/json'
      self.response.out.write(json.dumps(processor.response_list))

  @handle.util.param([('keg_id', int)])
  def put(self, **kwargs):
    self.verify_user()
    self.load_request()
    processor = process.KegUpdateProcessor(keg_id=self.keg_id, **self.request_object)
    self.response.content_type = 'application/json'
    self.response.out.write(json.dumps(processor.response_object))

  @handle.util.param([('keg_id', int)])
  def delete(self, **kwargs):
    self.verify_user()
    processor = process.KegDeleteProcessor(keg_id=self.keg_id)
    self.response.content_type = 'application/json'
    self.response.out.write(json.dumps(processor.response_object))

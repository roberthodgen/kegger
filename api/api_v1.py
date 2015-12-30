"""

api_v1

"""


import webapp2

import handle


routes = []

routes.append(webapp2.Route(
  '/api/v1/status',
  handler=handle.StatusRequestHandler,
  methods=['GET']
))

routes.append(webapp2.Route(
  '/api/v1/kegs',
  handler=handle.KegRequestHandler,
  methods=['GET', 'POST']
))

routes.append(webapp2.Route(
  '/api/v1/kegs/<keg_id:([\d]+)>',
  handler=handle.KegRequestHandler,
  methods=['GET', 'PUT', 'DELETE']
))

app = webapp2.WSGIApplication(routes)


app.error_handlers[400] = handle.util.http_400_bad_request
app.error_handlers[401] = handle.util.http_401_unauthorized
app.error_handlers[404] = handle.util.http_404_not_found
app.error_handlers[500] = handle.util.http_500_internal_server_error

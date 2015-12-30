"""

handle.util

"""


import config

import webapp2

import json

import logging

from ndb_users import users


def http_400_bad_request(request, response, exception):
    """ Return an HTTP 400 Bad Request status. """
    response_object = {
        'error': 'HTTP/1.1 400 Bad Request',
        'message': 'Missing parameter.',
        'type': type(exception).__name__,
        'exception': str(exception)
    }
    response.set_status(400)
    response.content_type = 'application/json'
    response.out.write(json.dumps(response_object))


def http_401_unauthorized(request, response, exception):
    """ Return an HTTP 401 Unauthorized status. """
    response_object = {
        'error': 'HTTP/1.1 401 Unauthorized',
        'message': 'Not logged in.',
        'type': type(exception).__name__,
        'exception': str(exception)
    }
    response.set_status(401)
    response.content_type = 'application/json'
    response.out.write(json.dumps(response_object))


def http_404_not_found(request, response, exception):
    """ Return an HTTP 404 Not Found status. """
    response_object = {
        'error': 'HTTP/1.4 404 Not Found',
        'message': 'Not found.',
        'type': type(exception).__name__,
        'exception': str(exception)
    }
    response.set_status(404)
    response.content_type = 'application/json'
    response.out.write(json.dumps(response_object))


def http_500_internal_server_error(request, response, exception):
    """ Return an HTTP 500 Internal Server Error status. """
    logging.exception(exception)
    response_object = {
        'error': 'HTTP/1.1 500 Internal Server Error',
        'message': 'Internal server error.',
        'type': type(exception).__name__,
        'exception': str(exception)
    }
    response.set_status(500)
    response.content_type = 'application/json'
    response.out.write(json.dumps(response_object))


def model_exception(request, response, exception):
    """ Return an HTTP 400 Bad Request status. """
    response_object = {
        'error': 'HTTP/1.1 404 Bad Request',
        'message': 'ModelException',
        'type': type(exception).__name__,
        'exception': str(exception)
    }
    response.set_status(400)
    response.content_type = 'application/json'
    response.out.write(json.dumps(response_object))


def handle_exception(request, response, exception):
    """ Return an HTTP 400 Bad Request status. """
    response_object = {
        'error': 'HTTP/1.1 404 Bad Request',
        'message': 'ModelException',
        'type': type(exception).__name__,
        'exception': str(exception)
    }
    response.set_status(400)
    response.content_type = 'application/json'
    response.out.write(json.dumps(response_object))


class HandleException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class RequestException(HandleException):
    pass


class UnauthorizedException(RequestException):
    pass


class BadRequestException(RequestException):
    pass


class InputMissingRequestException(BadRequestException):
    pass


class NotFoundException(RequestException):
    pass


def param(params):
    def _param(function):
        def _decorator(self, *args, **kwargs):
            for param in params:
                fn = False
                if type(param) is tuple:
                    fn = param[1]
                    param = param[0]
                val = kwargs.get(param)
                if fn and val:
                    val = fn(val)
                setattr(self, param, val)
            return function(self, *args, **kwargs)
        return _decorator
    return _param


class AbstractRequestHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        """ Handle an uncaught exception. """
        if isinstance(exception, webapp2.HTTPException):
            # Exceptions generated via `self.abort(000)`
            handle_exception(self.request, self.response, exception)
        elif isinstance(exception, UnauthorizedException):
            http_401_unauthorized(self.request, self.response, exception)
        elif isinstance(exception, RequestException):
            http_400_bad_request(self.request, self.response, exception)
        else:
            # Catch-all
            http_500_internal_server_error(self.request, self.response,
                exception)

    def verify_user(self):
        self.user = users.get_current_user()
        if not self.user:
            raise UnauthorizedException("Invalid or no user session provided.")

    def load_request(self):
        try:
            self.request_object = json.loads(self.request.body)
        except:
            raise BadRequestException("JSON POST body")


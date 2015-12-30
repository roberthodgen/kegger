(function () {

  var app = angular.module('roberthodgen.ndb-users', ['roberthodgen.angular-logger']);

  app.service('Users', ['$http', 'Log', function ($http, Log) {
    var self = this;


    /**
     * URL Constants
     */
    self.LOGIN_API_PATH                 = '/users/_login.json';
    self.LOGIN_CREATE_API_PATH          = '/users/_login/create.json';
    self.LOGIN_ACTIVATE_API_PATH        = '/users/_login/activate.json';
    self.LOGIN_PASSWORD_CHANGE_API_PATH = '/users/_login/password/change.json';
    self.LOGIN_PASSWORD_FORGOT_API_PATH = '/users/_login/password/forgot.json';
    self.LOGIN_PASSWORD_RESET_API_PATH  = '/users/_login/password/reset.json';


    /**
     * Users.cache
     * Responsible for storing the cached User object.
     */
    self.cache = null;


    /**
     * Get a log
     */
    var log = Log.createLogLevel({
      name: 'users',
      hooks: []
    });


    /**
     * Users.getCurrentUser
     * Returns a promise that resolves to an object for the current User or rejects with an explination.
     */
    self.getCurrentUser = function () {
      log('Users.getCurrentUser');
      if (self.cache) {
        return defer(self.cache);
      }

      return get(self.LOGIN_API_PATH);
    };


    /**
     * Users.createLoginUrl
     */
    self.createLoginUrl = function () {

    };


    /**
     * Users.createLogoutUrl
     */
    self.createLogoutUrl = function () {

    };


    /**
     * defer
     * Wraps an Object in a defer if obj is a user.
     */
    function defer (obj) {
      if (angular.isObject(obj) && isUser(obj.email)) {
        return $q.when(obj);
      }

      return $q.reject(obj);
    }


    function get (url, data) {
      return $http({
        method: 'GET',
        url: url,
        data: data
      }).then(cacheUser).then(function (response) {
        return response && response.user || {};
      });
    }


    function post (url, data) {
      return $http({
        method: 'POST',
        url: url,
        data: data
      }).then(cacheUser).then(function (response) {
        return response && response.user || {};
      });
    }


    /**
     * isUser
     * Checker function for whether a user object exists.
     */
    function isUser (obj) {
        return (angular.isObject(obj) && angular.isString(obj.email));
    }


    /**
     * cacheUser
     * Places the user object (if user is found) in the cache.
     */
    function cacheUser (response) {
      var data = response && response.data || {};
      if (angular.isObject(data) && isUser(data.user)) {
        self.cache = data.user;
      }

      return data;
    }

  }]);

})();

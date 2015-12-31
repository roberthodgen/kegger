(function () {

  var app = angular.module('roberthodgen.ndb-users', ['roberthodgen.angular-logger']);

  app.service('Users', ['$http', '$q', 'Log', function ($http, $q, Log) {
    var self = this;


    /**
     * URL Constants
     */
    self.LOGIN_API_PATH                 = '/users/login.json';
    self.LOGIN_CREATE_API_PATH          = '/users/login/create.json';
    self.LOGIN_ACTIVATE_API_PATH        = '/users/login/activate.json';
    self.LOGIN_PASSWORD_CHANGE_API_PATH = '/users/login/password/change.json';
    self.LOGIN_PASSWORD_FORGOT_API_PATH = '/users/login/password/forgot.json';
    self.LOGIN_PASSWORD_RESET_API_PATH  = '/users/login/password/reset.json';


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
     * Users.login
     * Returns a promise that resolves to an object for the current User or rejects with an explination.
     */
    self.login = function (email, password, extended) {
      extended = extended !== false;
      log('Users.login');
      return post(self.LOGIN_API_PATH, {
        email: email,
        password: password,
        extended: extended
      });

    };


    /**
     * defer
     * Wraps an Object in a defer if obj is a user.
     */
    function defer (obj) {
      if (angular.isObject(obj) && isUser(obj.user)) {
        return $q.when(obj.user);
      }

      return $q.reject(obj);
    }

    function deferFactory (response) {
      return defer(response);
    }


    function get (url, data) {
      return $http({
        method: 'GET',
        url: url,
        data: data
      }).then(cacheUser).then(deferFactory);
    }


    function post (url, data) {
      return $http({
        method: 'POST',
        url: url,
        data: data
      }).then(cacheUser).then(deferFactory);
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

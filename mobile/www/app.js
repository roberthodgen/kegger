(function () {

  var app = angular.module('kegger', [
    'ionic',
    'roberthodgen.angular-logger',

    'kegger.AppController',
    'kegger.KegsController',
    'kegger.KegController',
    'kegger.CreateController'
  ]);

  app.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
    // $stateProvider.state('login');

    $urlRouterProvider.when('', '/app');
    $urlRouterProvider.when('/app', '/app/kegs');

    $stateProvider.state('app', {
      abstract: true,
      url: '/app',
      controller: 'AppController',
      template: '<ion-nav-view></ion-nav-view>'
    });

    $stateProvider.state('app.kegs', {
      url: '/kegs',
      templateUrl: 'partials/kegs-controller.html',
      controller: 'KegsController'
    });

    $stateProvider.state('app.keg', {
      url: '/kegs/:kegId',
      templateUrl: 'partials/keg-controller.html',
      controller: 'KegController'
    });

    $stateProvider.state('app.create', {
      url: '/create',
      templateUrl: 'partials/create-controller.html',
      controller: 'CreateController'
    });
  }]);

  app.config(['LogProvider', function (LogProvider) {
    LogProvider.LOG_LEVELS = ['info', 'debug', 'warn', 'error'];
  }]);

  app.run(['Log', '$log', function (Log, $log) {
    Log.info.addHook($log.info);
  }]);

  app.run(['$ionicPlatform', function ($ionicPlatform) {
    $ionicPlatform.ready(function () {
      if (window.cordova && window.cordova.plugins.Keyboard) {
        cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
        cordova.plugins.Keyboard.disableScroll(true);
      }

      if (window.StatusBar) {
        StatusBar.styleDefault();
      }
    });
  }]);

})();

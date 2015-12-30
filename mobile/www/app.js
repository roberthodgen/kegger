(function () {

  var app = angular.module('kegger', [
    'ionic',

    'kegger.AppController'
  ]);

  app.run(['$ionicPlatform', function ($ionicPlatform) {
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);
    }

    if (window.StatusBar) {
      StatusBar.styleDefault();
    }
  }]);

})();

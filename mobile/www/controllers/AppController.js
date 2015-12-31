(function () {

	var app = angular.module('kegger.AppController', ['roberthodgen.ndb-users', 'roberthodgen.angular-logger', 'ngResource']);

	app.controller('AppController', ['$scope', 'Log', 'Users', function ($scope, Log, Users) {
		$scope.init = function () {
			Log.info('kegger.AppController: AppController $scope.init');

			$scope.user = {};

			Users.getCurrentUser().then($scope.userLoggedIn, $scope.userLoginFailure);
		};

		$scope.userLoggedIn = function (user) {
			Log.info('kegger.AppController: AppController $scope.userLoggedIn');
			$scope.user = user;
		};

		$scope.userLoginFailure = function (data) {
			debugger;
		};


		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

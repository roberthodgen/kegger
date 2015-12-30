(function () {

	var app = angular.module('kegger.AppController', ['roberthodgen.angular-logger', 'ngResource']);

	app.controller('AppController', ['$scope', 'Log', function ($scope, Log) {
		$scope.init = function () {
			Log.info('kegger.AppController: AppController $scope.init');
		};


		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

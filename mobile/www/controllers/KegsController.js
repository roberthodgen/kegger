(function () {

	var app = angular.module('kegger.KegsController', []);

	app.controller('KegsController', ['$scope', function ($scope) {
		var self = this;

		$scope.init = function () {
			Log.info('kegger.KegsController KegsController $scope.init');
		};

		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

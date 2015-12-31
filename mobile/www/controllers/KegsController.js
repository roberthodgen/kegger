(function () {

	var app = angular.module('kegger.KegsController', ['roberthodgen.angular-logger']);

	app.controller('KegsController', ['$scope', 'Log', 'Kegs', function ($scope, Log, Kegs) {
		var self = this;

		$scope.init = function () {
			Log.info('kegger.KegsController KegsController $scope.init');

			$scope.kegs = Kegs.query();
		};

		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

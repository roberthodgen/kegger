(function () {

	var app = angular.module('kegger.KegController', ['roberthodgen.angular-logger', 'kegger.resources']);

	app.controller('KegController', ['$scope', '$stateParams', 'Log', 'Kegs', function ($scope, $stateParams, Log, Kegs) {
		$scope.init = function () {
			Log.info('kegger.KegController KegController $scope.init');

			$scope.keg = Kegs.get({
				kegId: $stateParams.kegId
			});
		};


		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

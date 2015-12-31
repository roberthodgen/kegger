(function () {

	var app = angular.module('kegger.CreateController', ['roberthodgen.angular-logger', 'kegger.resources']);

	app.controller('CreateController', ['$scope', 'Log', 'BeerSearch', function ($scope, Log, BeerSearch) {
		$scope.init = function () {
			Log.info('kegger.CreateController CreateController $scope.init');
		};

		$scope.search = {};

		$scope.$watch('search.name', function (newName) {
			Log.info('new name: '+ newName);
			$scope.beers = BeerSearch.get({
				q: newName
			});
		});


		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

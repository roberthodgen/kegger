(function () {

	var app = angular.module('kegger.CreateController', ['roberthodgen.angular-logger', 'kegger.resources']);

	/**
	 * Time in MS to wait for user input before searching.
	 * (should greatly reduce BreweryDB API calls)
	 */
	app.constant('BEER_SEARCH_INPUT_TIMEOUT', 300);

	app.controller('CreateController', ['$scope', '$timeout', 'BEER_SEARCH_INPUT_TIMEOUT', 'Log', 'BreweryDbSearch', function ($scope, $timeout, BEER_SEARCH_INPUT_TIMEOUT, Log, BreweryDbSearch) {
		var self = this;

		self.beerSearchTimeout = null;

		self.beerSearch = function () {
			var name = $scope.search.name;

			if (!angular.isString(name) || name.length === 0) {
				$scope.beers = [];
				return;
			}

			Log.info('kegger.CreateController CreateController.beerSearch initiated');
			$scope.beers = BreweryDbSearch.query({
				q: $scope.search.name
			});
		};

		$scope.init = function () {
			Log.info('kegger.CreateController CreateController $scope.init');

			$scope.search = {
				name: ''
			};
		};

		$scope.beerSearch = function () {
			if (self.beerSearchTimeout !== null) {
				$timeout.cancel(self.beerSearchTimeout);
			}

			self.beerSearchTimeout = $timeout(self.beerSearch, BEER_SEARCH_INPUT_TIMEOUT);
		};

		$scope.$on('$destroy', function () {
			$timeout.cancel(self.beerSearchTimeout);
			self.beerSearchTimeout = null;
		});


		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

(function () {

	var app = angular.module('kegger.CreateController', ['roberthodgen.angular-logger']);

	app.controller('CreateController', ['$scope', 'Log', '$resource', function ($scope, Log, $resource) {
		var Search;

		$scope.init = function () {
			Log.info('kegger.CreateController CreateController $scope.init');

			Search = $resource('mock/search.json', {
				key: 'abc123'
			});
		};

		$scope.search = {};

		$scope.$watch('search.name', function (newName) {
			Log.info('new name: '+ newName);
			$scope.beers = Search.get({
				q: newName
			});
		});


		/**
		 * Init
		 */
		$scope.init();
	}]);

})();

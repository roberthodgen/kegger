(function () {

	var app = angular.module('kegger.resources', ['ngResource', 'kegger.api-keys']);

	app.factory('BreweryDbSearch', ['BREWERY_DB_API_KEY', '$resource', function (BREWERY_DB_API_KEY, $resource) {
		return $resource('/brewerydb/search', {
			key: BREWERY_DB_API_KEY
		}, {
			query: {
				isArray: false
			}
		});
	}]);

})();

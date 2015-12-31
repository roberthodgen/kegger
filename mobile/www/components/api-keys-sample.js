/**
 * Rename the file to `api-keys.js` (remove `-sample`)!!
 */

(function () {

	var app = angular.module('kegger.api-keys', []);

	/**
	 * Careful not to commit API keys!!
	 */
	app.constant('BREWERY_DB_API_KEY', '**KEY HERE**');

})();

# kegger

> GAE backend


## To run:

1. Install App Engine SDK: https://cloud.google.com/appengine/downloads
2. (in the `api` directory) launch the development app server: `dev_appserver.py app.yaml`
3. Login via `/_login` or JSON API.


## Keg Object

E.g.:
```
{
	"id": 1234567890,
	"name": "Big Salty Lager",
	"created": "2015-12-30T04:31:42.964626+00:00",
	"updated": "2015-12-30T04:31:42.964626+00:00",
	"capacity": 314.15,
	"consumed": 32,
	"unit": "oz"
}
```


### Keg Properties

`id` unique integer id for the Keg, read-only.

`name` string, read/write.

`created` timestamp when the Keg was created, read-only.

`updated` timestamp when the Keg was last updated, read-only.

`capacity` float capacity of the Keg, read/write.

`consumed` float amout consumed of the Keg, read/write.

`unit` string, read/write. Options: `oz`, `ml`, `l`


## Check a user's kegs

`GET /api/v1/kegs`

Returns a array of Keg objects or empty array if no kegs exist.


## Create Keg

`POST /api/v1/kegs`

Keg object without `id`, `created`, or `updated` properties.

Example:
```
{
	"name": "New Brewski",
	"capacity": 123.456
	"unit": "l"
}
```


## Update Keg

`PUT /api/v1/kegs/:keg_id`

Example: Update the Keg's `consumed` to 48:
```
{
	"consumed": 48
}
```


# Single Keg

`GET /api/v1/kegs/:keg_id`

Should return a Keg object.

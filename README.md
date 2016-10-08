# strava2excel
Very very simple tool to export basic data about Strava activities to an excel spreadsheet

## Usage
Download file strava2excel.py and run the export function. See, easy and simple

To see more about the export function, see Documentation.
## Dependencies
* pandas
* stravalib


## How to get Strava API Access
Go to [your API application page](https://www.strava.com/settings/api): https://www.strava.com/settings/api
Fill out with the following information:
* Application Name: Choose any name
* Website: https://strava.com
* Application Description: Whatever description you want
* Authorization Callback Domain: localhost

## Strava API Rate Limiting
Strava only allows 600 requests every 15 minutes and 30,000 requests daily. Of course, you are running this with your own API token, so it all depends on how many activities you may have. Hopefully, I will add some functionality in the future so that output of the pulled activities will be visible without having to wait 15 minutes (or until midnight UTC)

## Future improvements
* Adding new activities to the same file instead of having to pull them all back again
* CSV Export
* Strava API rate limiting helper
* Caching activities
* Sheet with Segment info
* Sheet with Gear info

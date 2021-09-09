# Finsure Tech Challenge

## Master Branch: Initial commit

This contains the foundation of the backend, everything I need to start working on the API has been set up.

- configuring the MariaDB database to the backend
- linking the urls
- configuration of backend done by .env

Setting this all up took a little longer than I initially thought it would, I had trouble with the installation of MariaDB it had taken me about 3 hours to scan through the log files and fix a configuration issue between the mysql-client and mysql-server.

## FEATURE/database_model Branch: Created Lender model

I created the Lender Model and configured it to the admin site for manual testing, the model has some basic data valitation to make sure that potential data falls in the scope of what is suppose to be in the database.

## FEATURE/endpoints Branch: Outlined API endpoints

I prepared all of the endpoint urls, a serializer for the model and added a docstring to each endpoint describing the functionality, now the endpoints need to just have their functionality added.

## FEATURE/endpoints Branch: Implemented list pages functionality

I made 2 diffrent endpoints for listing pages one returns a group of 5 lenders per page regardless of active status and the other only returns those with an active status. a querystring is used to determine which page the url looks like this:

`/lenders/list?page=1`

The hardest part of doing these endpoints was figuring out how to convert a QuerySet of Model objects into a json serializable format.

## FEATURE/endpoints Branch: Refactored list lenders endpoint

After sleeping on it, I figured out how to make listing lenders and listing active lenders alot neater I also found an edgecase that I had initially missed as well as clearing up unused imports and dependencies.

## FEATURE/endpoints Branch: Added download lenders in csv format

Due to the commonality of this desired functionality, there was a lot of documentation and tutorials, this ended up being easier than I first thought.

## FEATURE/endpoints Branch: Added upload lenders in csv format

Now can bulk upload lenders to the database using a post request to `/lenders/upload` with a multipart form body with the name 'lenders' and a csv file.

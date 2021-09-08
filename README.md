# Finsure Tech Challenge

## Commit 1: Initial commit

This contains the foundation of the backend, everything I need to actually start working on the API has been setup.

- configuring the MariaDB database to the backend
- linking the urls
- configuration of backend done by .env

Setting this all up took a little longer than I initaly thought it would, I had trouble with the installation of MariaDB it had taken me about 3 hours to scan through the log files and fix a configuration issue between the mysql-client and mysql-server.

## Commit 2: Created Lender model

I created the Lender Model and configured it to the admin site for manual testing, the model has some basic data valitation to make sure that potential data falls in the scope of what is suppose to be in the database.

## FEATURE/endpoints: Outlined API endpoints

I prepared all of the endpoint urls, a serializer for the model and added a docstring to each endpoint describing the functionality, now the endpoints need to just have their functionality added.
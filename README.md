# Finsure Tech Challenge

## Commit 1: Initial commit

This contains the foundation of the backend, everything I need to actually start working on the API has been setup.

- configuring the MariaDB database to the backend
- linking the urls
- configuration of backend done by .env

Setting this all up took a little longer than I initaly thought it would, I had trouble with the installation of MariaDB it had taken me about 3 hours to scan through the log files and fix a configuration issue between the mysql-client and mysql-server.

## Commit 2: Created Lender model

I created the Lender Model and configured it to the admin site for manual testing, the model has some basic data valitation to make sure that potential data falls in the scope of what is suppose to be in the database.

## FEATURE/tests Branch: Created tests for CRUD endpoints

Created tests for:

- creating an lender
- getting a single lender
- updating a lender: both partial & full
- deleting a lender

The tests cover basic edge cases but may be expanded upon if I discover issues when doing manual testing of the endpoints.
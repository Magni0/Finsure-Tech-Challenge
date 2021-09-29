# Finsure Tech Challenge

## TO DO

1. add more flexability to page size for pagination ✓
2. optimize the database query for pagination ✓
3. fix urls to make it RESTful ✓
4. fix views to make them RESTful ✓
5. implement Multithreading into bulk upload view
6. fix response json in views to make it RESTful

## Installation instructions

1. Clone the repository, uncompress the archive and navigate into the root directory from in the terminal
2. Create a python virtual environment using `python -m venv venv`
3. Activate the environment by typing `source venv/bin/activate` for Linux or `source venv/scripts/activate` for windows
4. Install app dependencies with `python -m pip install --upgrade pip && pip install -r requirements.txt`
5. Then you can run the development server with `python manage.py runserver`
    1. If you wish to have some dummy data, type the command `python manage.py loaddata lenders.json`

### URL paths

1. Create a new lender `lenders/create`
    1. Request body example:
       {
       "name": "Tommy Richard Nguyen",
       "code": "TRN",
       "upfront_commission_rate": 1.36,
       "trial_commission_rate": 1.10,
       "active": true
       }
2. List lenders in page `/lenders/list?page={page number}`
    1. if you want only active lenders `/lenders/list?page={page number}&active=true`
3. Get a specific lender `lenders/get/{id of lender}`
4. Update a specific lender `lenders/update/{id of lender}`
    1. Using the PATCH method will allow a partial update
    2. Using the PUT method will require all fields to update
5. Delete a specific lender `lenders/delete/{id of lender}`
6. Bulk upload lenders in csv format `lenders/upload`
    1. Body must be multipart form with the name being 'lenders'
7. Bulk download lenders to csv file `lenders/download`

## Commit history thought process

Below gives more insight into my thought process while working through this project

### Master Branch: Initial commit

This contains the foundation of the backend, everything I need to start working on the API has been set up.

-   configuring the MariaDB database to the backend
-   linking the urls
-   configuration of backend done by .env

Setting this all up took a little longer than I initially thought it would, I had trouble with the installation of MariaDB it had taken me about 3 hours to scan through the log files and fix a configuration issue between the mysql-client and mysql-server.

### FEATURE/database_model Branch: Created Lender model

I created the Lender Model and configured it to the admin site for manual testing, the model has some basic data validation to make sure that potential data falls within the scope of what is supposed to be in the database.

### FEATURE/tests Branch: Created tests for CRUD endpoints

Created tests for:

-   creating a lender
-   getting a single lender
-   updating a lender: both partial & full
-   deleting a lender

The tests cover basic edge cases but maybe expanded upon if I discover issues when doing manual testing of the endpoints.

### FEATURE/endpoints Branch: Outlined API endpoints

I prepared all of the endpoint urls, a serializer for the model, and added a docstring to each endpoint describing the functionality, now the endpoints need to just have their functionality added.

### FEATURE/endpoints Branch: Implemented list pages functionality

I made 2 different endpoints for listing pages one returns a group of 5 lenders per page regardless of active status and the other only returns those with an active status. a querystring is used to determine which page the url looks like this:

`/lenders/list?page=1`

The hardest part of doing these endpoints was figuring out how to convert a QuerySet of Model objects into a json serializable format.

### FEATURE/endpoints Branch: Refactored list lenders endpoint

After sleeping on it, I figured out how to make listing lenders and listing active lenders a lot neater I also found an edge-case that I had initially missed as well as clearing up unused imports and dependencies.

### FEATURE/endpoints Branch: Added download lenders in csv format

Due to the commonality of this desired functionality, there was a lot of documentation and tutorials, this ended up being easier than I first thought.

### FEATURE/endpoints Branch: Added upload lenders in csv format

Now can bulk upload lenders to the database using a post request to `/lenders/upload` with a multipart form body with the name 'lenders' and a csv file.

### FEATURE/tests Branch: Added test for bulk csv download

I made a basic test for the csv download endpoint that just checks that it returns the correct status code and I made a test for the upload as well however that is commented out at the moment as it is not working, I need to figure out how to properly mimic uploading a csv file as it's currently throwing a data type error. I know that the bulk upload csv endpoint is working from manual testing even though this test is tacking up an unreasonable amount of time to get it working, at this point I would ask for help instead of using up more time.

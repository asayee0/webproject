# Project URLs
heroku: https://reddit-content-filter.herokuapp.com/

github: https://github.com/asayee0/webproject

### NO ADDITIONAL CREDENTIALS ARE REQUIRED TO RUN THIS APP
The test credentials are provided in redditScraper.py line 6

# Running the app locally
To run the app locally: 
1. Install the requirements with `pip3 install -r requirements.txt`
2. Run the application with `FLASK_APP=app.py flask run`
3. Open the web app in local browser http://127.0.0.1:5000/

# CS Topic
This app was built to solve the problem of modularity of the Reddit search engine. It was built on the idea that subreddit administrators need to
keep track of negative content to maintain a better community. Redditors can search for keywords with the basic application, as well as add their
own custom code to the application in order to change the functionality or add modules such as Natural Language Processing to it. It acts as a 
foundation for web developers and subreddit admininstrators to be able to interchange and adapt particular aspects of the search engine to be 
able to tailor it to their needs.

# Implemented Features & Line #
## REST Services 
1. Perform GET request generated from developed API | redditScraper.py, line 14
2. Perform POST request from developed API
3. Perform DELETE request from developed API
4. Create two GET request | app,py, line 38
5. Create two POST requests | app.py, line 43
6. Create one PUT request
7. Create one DELETE request | app.py, line 69
8. Accept at least two parameters from client | app.py, line 25
9. At least two methods should be authenticated
10. Utilization of session within the developed API | redditScraper.py, line 6

## Database Connectivity 
1. Successfully connect to database | init.py, line 7
2. Create user with associated database
3. Insert data into the database | app.py, line 49
4. Read data from database | app.py, line 39
5. Utilization of Limit & Offset

## Cloud
1. Successfully deployed to a cloud-based solution (i.e. Heroku, Digital Ocean, Firebase) | https://reddit-content-filter.herokuapp.com/
3. Database online
4. Accessible online

## Data Visualization
1. Successfully Implementation of at least one visualization
2. Applicability to the problem
3. AJAX based information

## CS Topic
1. Modularity / Scalability / Efficiency / Extensibility
2. Identification of at least one CS topic
3. Justification of the design factors selected

## IO Problem
1. Solution
2. Innovative
3. Works as Described


## Created by Asa Yee (815009011)
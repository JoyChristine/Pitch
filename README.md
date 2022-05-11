
## Description

Pitch is a web application that will help users list and preview pitches in different categories.


## Features
A user can;
*  See the pitches other people have posted.
* Vote on the pitch they liked and give it a downvote or upvote.
* Sign in & leave a comment
* Receive a welcoming email once I sign up.
* View the pitches I have created in my profile page.
* Comment on the different pitches and leave feedback.
* Submit a pitch in any category.
* View the different categories.


<!-- # Behavior Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View All News Sources | Default Home Page(right)| Displays all news sources |
|View Top Headlines | Default home page (left)| Displays Top Headlines articles |
| View Categories of news sources| Click on any category on teh navbar | Redirects to the specified category articles page|
| Search for an article by keyword | Type any keyword in `search bar` e.g. `Kenya`| Redirects to search page with all the search results for Kenya|

## View Live Site here
View the complete site [here](https://newsapp-joy.herokuapp.com/) -->


## Technologies Used
    - Python 3.8
    - Flask Framework
    - HTML, CSS and Bootstrap
    
    
## Set-up and Installation
Prepare the environment variables.

    (virtual)$exportDATABASE_URL='postgresqlpsycopg2://username:password@localhost/pitch'`<br/>
    `(virtual)$ export SECRET_KEY='Your secret key'

Run Database Migrations.

    (virtual)$ python manage.py db init
    (virtual)$ python manage.py db migrate -m "Initial migration"
    (virtual)$ python manage.py db upgrade

Run the app.

    (virtual)$ touch start.sh

    Put #!/usr/bin/env bash as the first line in start.sh
    Put python3.8 manage.py server as the second line in start.sh

    (virtual)$ chmod a+x start.sh
    (virtual)$ ./start.sh


## Contributors
    - Joy Christine Nduta Kimani

### Contact Information
joychristin2@gmail.com

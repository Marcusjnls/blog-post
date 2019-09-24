# **BlogPost**

### September 24th, 2019
#### By **[Marcus Jean-Louis](https://github.com/marcusjnls)**

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Project Description

This is a web-app where users can come and share their ideas on how they can best blog an idea to potential investors. Users can then have those blogs commeted on and share better ways of imporving on their blogs

-   Users can **add** and **delete** blogs _the deleting part is not yet implemented_ - thuis feature can only be accessed by users who are logged in. If you don't have an account you can navigate to the signup page and crate a new account

-   Users also get to see how long ago a blog was posted

-   users can also **upvote** and **downvote** blogs that they like or don't like.

-   users can leave comments on quotes _it is advisable that this featre be used aacordingly and appropriately_

-   later plans include choosing quotes of the day based on quotes with the best _upvote to downvote ration_

-   On the home page there is a image slider that shows users what the benefits of using the website are and motivate them to sign up imediately

-   Users who have signed in get a dashboard where they can manage their posts including **Editing**, **Deleting**, _a future plan include adding a statistics section where users can see the progress of their posts_

-   Finally is to add a section where users can **_Delete Their Accounts_** if they want to. Password confirs=mation will be required for this step to work

## Set up instructions

### Prerequiites
    - Python 3.6
    - Ubuntu software

Click here to visit the [Git Hub](https://github.com/marcusjnls/blog-post) repository for the project.

## Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Marcusjnls/blog-post.git && cd blog-post`

Install [Postgres](https://www.postgresql.org/download/)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
export SECRET_KEY='Your secret key'
```

### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```

### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

## Support and contact details
Contact me for any comments, reviews or advice;
Name: Marcus Jean-Louis
Phone: 0722-894999
Email: marcusjnls@gmail.com

### License
Copyright (c) **Marcus Jean-Louis**
